from django.db import models

from ChargingStation.models import ChargingStation

class EnergyProviderManager(models.Manager):
    def create_energy_provider(self, name, availability, price):
        energy_provider = self.create(name=name, availability=availability, price=price)
        return energy_provider

class EnergyProviderInterface(models.Model):
    name = models.CharField(max_length=255)
    availability = models.BooleanField()
    price = models.FloatField()
    objects = EnergyProviderManager()

    class Meta:
        abstract = True

    def get_name(self):
        return self.name

    def get_availability(self):
        return self.availability
    
    def get_price(self):
        return self.price


class DSOManager(models.Manager):
    def create_dso(self, name, availability, price):
        dso=DSO(name=name, availability=availability, price=price)
        dso.save()
        
        return dso

class DSO(EnergyProviderInterface):
    objects = DSOManager()

class BSSManager(models.Manager):
    def create_bss(self, **kwargs):
        bss = self.create(**kwargs)
        return bss

class BSS(EnergyProviderInterface):
    station = models.OneToOneField(ChargingStation, 
        on_delete=models.CASCADE, 
        related_name='connected_bss',
        default=None)
    capacity = models.IntegerField(default=None)
    currentEnergy = models.IntegerField(default=0)
    isActive = models.BooleanField(default=True)
    objects = BSSManager()

    def get_capacity(self):
        return self.capacity

    def get_station(self):
        return self.station