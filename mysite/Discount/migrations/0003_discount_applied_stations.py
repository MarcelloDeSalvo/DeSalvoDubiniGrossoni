# Generated by Django 4.1.5 on 2023-01-22 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChargingStation', '0001_initial'),
        ('Discount', '0002_alter_discount_discount_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='applied_stations',
            field=models.ManyToManyField(to='ChargingStation.chargingstation'),
        ),
    ]
