from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe

from django.db import models

from .models import Client, Location, Avis, Vehicule, Document, Photo, Location_Vehicule, Dommage, Maintenance

class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            output.append(
                f'<a href="{image_url}" target="_blank">'
                f'<img src="{image_url}" width="50" height="50" '
                f'style="object-fit: cover;"/> </a>')
        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        return mark_safe(u''.join(output))

class PhotoInline(admin.TabularInline):
    model = Photo
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }
    extra = 0

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'tel', 'adresse']
    search_fields = ['username', 'email', 'tel']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'dateLocation', 'statut']
    search_fields = ['client__username', 'statut']

@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ['id', 'immatriculation', 'marque', 'modele', 'prix']
    search_fields = ['immatriculation', 'marque', 'modele']
    inlines = [PhotoInline]

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'vehicule', 'nom', 'dateEmission', 'dateValidite']
    search_fields = ['nom', 'vehicule__immatriculation']

@admin.register(Dommage)
class DommageAdmin(admin.ModelAdmin):
    list_display = ['id', 'location_vehicule', 'description']
    search_fields = ['description']

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'dommage', 'montant', 'dateEntree', 'dateSortie']
    search_fields = ['dommage__description'] 