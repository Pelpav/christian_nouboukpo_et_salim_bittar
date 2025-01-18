import json
from django.shortcuts import get_object_or_404, render, redirect
from back.models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Créer vos vues ici.
def home(request):
    vehicules = Vehicule.objects.all()[:3]  # Exemple pour limiter à 3 échantillons
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

# Nouvelles vues pour le panier et le paiement
def cart(request):
    return render(request, 'front/cart.html')

@login_required
@csrf_exempt
def checkout(request):
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

@login_required
@csrf_exempt
def validation(request):
    vehicle_ids = json.loads(request.POST.get('vehicle_ids', '[]'))
    if not vehicle_ids:
        return redirect('checkout')

    # Vérifier si l'utilisateur a un profil Client
    try:
        client = request.user.client
    except Client.DoesNotExist:
        return redirect('register')  # ou une autre page appropriée

    # Créer une nouvelle location
    location = Location.objects.create(
        client=client,
        dateLocation=timezone.now(),
        dateSortie=timezone.now(),
        dateRetour=timezone.now() + timezone.timedelta(days=1),
        statut='En attente',
        adresseLivraison='Parking'
    )

    # Mettre à jour la base de données pour confirmer la location
    location.statut = 'Validé'
    location.datePaiement = timezone.now()
    location.save()

    # Mettre à jour Location_Vehicule pour chaque véhicule
    for vehicle_id in vehicle_ids:
        vehicule = get_object_or_404(Vehicule, id=vehicle_id)
        Location_Vehicule.objects.create(
            location=location,
            vehicule=vehicule,
            etatSortie='Validé',
            etatRetour='En attente'
        )

    # Rediriger vers une page de confirmation
    return redirect('home')
