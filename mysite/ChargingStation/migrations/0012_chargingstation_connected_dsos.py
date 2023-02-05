# Generated by Django 4.1.5 on 2023-01-24 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnergyProvider', '0005_remove_dso_station'),
        ('ChargingStation', '0011_rename_activedso_chargingstation_active_dso'),
    ]

    operations = [
        migrations.AddField(
            model_name='chargingstation',
            name='connected_dsos',
            field=models.ManyToManyField(related_name='connected_dso', to='EnergyProvider.dso'),
        ),
    ]