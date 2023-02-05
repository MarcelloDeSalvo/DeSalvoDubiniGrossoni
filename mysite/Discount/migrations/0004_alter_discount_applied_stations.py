# Generated by Django 4.1.5 on 2023-01-22 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChargingStation', '0001_initial'),
        ('Discount', '0003_discount_applied_stations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='applied_stations',
            field=models.ManyToManyField(related_name='applied_stations', to='ChargingStation.chargingstation'),
        ),
    ]