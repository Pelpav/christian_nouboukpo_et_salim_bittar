from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from django.db import models

from .models import Location, Avis, Vehicule, Document, Photo, Location_Vehicule, Dommage, Maintenance

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
    fields = ['indication', 'src', 'url']  # Ajoutez le champ URL ici
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }
    extra = 0

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'dateLocation', 'statut']
    search_fields = ['client__username', 'statut']

@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):  # Assurez-vous que cela hérite de ModelAdmin
    list_display = ['id', 'get_vehicule_nom', 'prix']
    search_fields = ['immatriculation', 'marque', 'modele']
    inlines = [PhotoInline]

    def get_vehicule_nom(self, obj):
        return f"{obj.marque} {obj.modele}"
    get_vehicule_nom.short_description = 'Véhicule'

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_vehicule_nom', 'nom', 'dateEmission', 'dateValidite']
    search_fields = ['nom', 'vehicule__immatriculation']

    def get_vehicule_nom(self, obj):
        return f"{obj.vehicule.marque} {obj.vehicule.modele}"
    get_vehicule_nom.short_description = 'Véhicule'

@admin.register(Dommage)
class DommageAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_vehicule_nom', 'description']
    search_fields = ['description']

    def get_vehicule_nom(self, obj):
        return f"{obj.location_vehicule.vehicule.marque} {obj.location_vehicule.vehicule.modele}"
    get_vehicule_nom.short_description = 'Véhicule'

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_vehicule_nom', 'montant', 'dateEntree', 'dateSortie']
    search_fields = ['dommage__description']

    def get_vehicule_nom(self, obj):
        return f"{obj.dommage.location_vehicule.vehicule.marque} {obj.dommage.location_vehicule.vehicule.modele}"
    get_vehicule_nom.short_description = 'Véhicule'