from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


class Client(User):
    # Champs hérités de User
    # username = models.CharField(max_length=150, unique=True)  # Nom d'utilisateur
    # first_name = models.CharField(max_length=30, blank=True)  # Prénom
    # last_name = models.CharField(max_length=150, blank=True)  # Nom
    # email = models.EmailField(blank=True)  # Email
    # password = models.CharField(max_length=128)  # Mot de passe
    # is_active = models.BooleanField(default=True)  # Actif
    # is_staff = models.BooleanField(default=False)  # Membre du personnel
    # is_superuser = models.BooleanField(default=False)  # Super utilisateur
    # last_login = models.DateTimeField(null=True, blank=True)  # Dernière connexion
    # date_joined = models.DateTimeField(auto_now_add=True)  # Date d'inscription

    # Champs spécifiques à Client
    tel = models.CharField(max_length=20)  # Numéro de téléphone
    adresse = models.TextField()  # Adresse
    numPieceID = models.CharField(max_length=50, unique=True)  # Numéro de pièce d'identité
    typePieceID = models.CharField(max_length=50)  # Type de pièce d'identité
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)  # Photo optionnelle

    @property
    def img_display(self):
        return mark_safe('<img src="{url}" width="50" height="50" />'.format(
            url=self.photo.url if self.photo else ''
        ))