import json
from django.shortcuts import get_object_or_404, render, redirect
from back.models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

def check_login(request):
    if not request.user.is_authenticated:
        return redirect('/login')

def home(request):
    vehicules = Vehicule.objects.all()[:3]
    avis_clients = Avis.objects.all()
    return render(request, 'front/home.html', {
        'services': services,
        'vehicules': vehicules,
        'avis_clients': avis_clients
    })

def about(request):
    return render(request, 'front/about.html')

def contact(request):
    return render(request, 'front/contact.html')

def cars(request):
    vehicules = Vehicule.objects.all()
    return render(request, 'front/cars.html', {'vehicules': vehicules})

def services(request):
    return render(request, 'front/services.html')

def blog(request):
    return render(request, 'front/blog.html')

def vehicle_details(request, id):
    vehicule = get_object_or_404(Vehicule, id=id)
    return render(request, 'front/details.html', {'vehicule': vehicule})

def cart(request):
    return render(request, 'front/cart.html')

@csrf_exempt
def checkout(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    check_login(request)
    if request.method == 'POST':
        cart = json.loads(request.body) if request.body else []
        vehicle_ids = [item['id'] for item in cart]
        return redirect('validation', vehicle_ids=vehicle_ids)
    return render(request, 'front/checkout.html')

def get_vehicle_details(request):
    vehicle_ids = request.GET.getlist('ids[]')
    vehicles = Vehicule.objects.filter(id__in=vehicle_ids)
    vehicle_data = [
        {
            'id': vehicle.id,
            'name': f"{vehicle.marque} {vehicle.modele}",
            'price': vehicle.prix
        }
        for vehicle in vehicles
    ]
    return JsonResponse({'vehicles': vehicle_data}) 

@csrf_exempt
def validation(request):
    cart = json.loads(request.body) if request.body else []  # Changer pour utiliser request.body
    vehicle_ids = [vehicle_id for vehicle_id in cart]  # Récupérer les IDs des véhicules à partir du panier

    if not vehicle_ids:
        return redirect('checkout')

    client = get_object_or_404(Client, id=request.user.id)  # Récupérer le client à partir du modèle Client

    try:
        location = Location.objects.create(
            client=client,
            dateLocation=timezone.now(),
            dateSortie=timezone.now(), 
            datePaiement=timezone.now(),
            dateRetour=timezone.now() + timezone.timedelta(days=1),
            statut='En attente',
            adresseLivraison='Parking'
        )
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

    location.statut = 'Validé'
    location.save()

    for vehicle_id in vehicle_ids:
        vehicule = get_object_or_404(Vehicule, id=vehicle_id)
        Location_Vehicule.objects.create(
            location=location,
            vehicule=vehicule,
            etatSortie='Validé',
            etatRetour='En attente'
        )

    # Vider le panier après validation
    # Remplacer l'appel à localStorage par une redirection vers le front-end pour vider le panier
    response = redirect('home')
    response.delete_cookie('cart')  # Supprimer le cookie du panier
    return response

def my_locations(request):
    locations = Location.objects.filter(client=request.user)
    return render(request, 'front/my_locations.html', {'locations': locations})

def submit_review(request, location_id):
    if request.method == 'POST':
        location = get_object_or_404(Location, id=location_id)
        commentaire = request.POST.get('commentaire')
        note = request.POST.get('note')
        
        # Créer un nouvel avis
        avis = Avis(location=location, commentaire=commentaire, note=note)
        avis.save()
        
        return redirect('my_locations')  # Rediriger vers la page des locations après soumission
    else:
        return HttpResponse("Méthode non autorisée", status=405)
    
    