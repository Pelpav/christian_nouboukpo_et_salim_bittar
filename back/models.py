from django.db import models
from django.utils.safestring import mark_safe
from django.core.validators import MinValueValidator, MaxValueValidator
from myauth.models import Client  # Correction de l'importation

class Location(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)
    dateLocation = models.DateTimeField()
    datePaiement = models.DateTimeField()
    dateSortie = models.DateTimeField()
    dateRetour = models.DateTimeField()
    statut = models.CharField(max_length=50, default='En attente')
    adresseLivraison = models.CharField(max_length=255, default='Parking')

    def total(self):
        # Calculer le total ici
        duree = (self.dateRetour - self.dateSortie).days
        total = duree * self.vehicule.prix
        return total

class Avis(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=None)
    note = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    commentaire = models.TextField()

class Vehicule(models.Model):
    immatriculation = models.CharField(max_length=50, unique=True)
    prix = models.IntegerField()
    etat = models.CharField(max_length=50)
    description = models.TextField()
    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    couleur = models.CharField(max_length=50)
    carburant = models.CharField(max_length=50)
    boitevitesse = models.CharField(max_length=50)
    climatisation = models.BooleanField(default=True)
    nbrRoues = models.IntegerField(default=4)
    nbrPlaces = models.IntegerField(default=5)
    nbrPortes = models.IntegerField(default=5)
    kilometrage = models.FloatField()
    cylindre = models.FloatField()
    anneeFabrication = models.IntegerField()
    anneeCirculation = models.IntegerField()

class Document(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, default=None)    
    nom = models.CharField(max_length=255)
    dateEmission = models.DateTimeField()
    dateValidite = models.DateTimeField()
    src = models.FileField(upload_to='documents/')

class Photo(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, null=True, blank=True, default=None)
    indication = models.CharField(max_length=255)
    src = models.ImageField(upload_to='photos/', blank=True, null=True)  
    url = models.URLField(blank=True, null=True)  

    @property
    def img_display(self):
        return mark_safe('<img src="{url}" width="50" height="50" />'.format(
            url=self.src.url if self.src else self.url if self.url else ''
        ))

class Location_Vehicule(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=None)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, default=None)
    etatSortie = models.CharField(max_length=255, default='En attente')
    etatRetour = models.CharField(max_length=255, default='En attente')

class Dommage(models.Model):
    location_vehicule = models.ForeignKey(Location_Vehicule, on_delete=models.CASCADE, default=None)
    description = models.TextField()
    photo = models.ImageField(upload_to='dommages/')

class Maintenance(models.Model):
    dommage = models.ForeignKey(Dommage, on_delete=models.CASCADE, default=None)
    causes = models.TextField()
    traitement = models.TextField()
    montant = models.IntegerField()
    dateEntree = models.DateTimeField()
    dateSortie = models.DateTimeField()
    preuves = models.FileField(upload_to='maintenances/') 