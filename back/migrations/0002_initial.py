# Generated by Django 5.1.4 on 2025-01-18 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('back', '0001_initial'),
        ('myauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myauth.client'),
        ),
        migrations.AddField(
            model_name='avis',
            name='location',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='back.location'),
        ),
        migrations.AddField(
            model_name='location_vehicule',
            name='location',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='back.location'),
        ),
        migrations.AddField(
            model_name='dommage',
            name='location_vehicule',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='back.location_vehicule'),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='dommage',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='back.dommage'),
        ),
        migrations.AddField(
            model_name='photo',
            name='vehicule',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='back.vehicule'),
        ),
        migrations.AddField(
            model_name='location_vehicule',
            name='vehicule',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='back.vehicule'),
        ),
        migrations.AddField(
            model_name='document',
            name='vehicule',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='back.vehicule'),
        ),
    ]
