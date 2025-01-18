from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


class Client(User):
    tel = models.CharField(max_length=20)
    adresse = models.TextField()
    numPieceID = models.CharField(max_length=50, unique=True)
    typePieceID = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/')

    @property
    def img_display(self):
        return mark_safe('<img src="{url}" width="50" height="50" />'.format(
            url=self.photo.url if self.photo else ''
        ))