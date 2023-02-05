# Generated by Django 4.1.5 on 2023-01-24 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnergyProvider', '0005_remove_dso_station'),
        ('ChargingStation', '0013_alter_chargingstation_active_dso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargingstation',
            name='connected_dsos',
            field=models.ManyToManyField(related_name='connected_dsos', to='EnergyProvider.dso'),
        ),
    ]