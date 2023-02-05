# Generated by Django 4.1.5 on 2023-01-21 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ChargingStation', '0001_initial'),
        ('Booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='start_time',
        ),
        migrations.AddField(
            model_name='booking',
            name='chargingStation',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ChargingStation.chargingstation'),
        ),
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.TimeField(default=None),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.EmailField(default=None, max_length=255, unique=True, verbose_name='email address'),
        ),
    ]