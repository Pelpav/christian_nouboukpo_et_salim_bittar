# Generated by Django 5.1.4 on 2025-01-18 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location_vehicule',
            name='etatRetour',
            field=models.CharField(default='En attente', max_length=255),
        ),
        migrations.AlterField(
            model_name='location_vehicule',
            name='etatSortie',
            field=models.CharField(default='En attente', max_length=255),
        ),
    ]
