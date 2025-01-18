from django.contrib import admin
from .models import Client

# Vérifiez si le modèle est déjà enregistré avant de l'enregistrer

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('username', 'tel', 'adresse', 'numPieceID', 'typePieceID', 'img_display')
    search_fields = ('username', 'tel', 'numPieceID')