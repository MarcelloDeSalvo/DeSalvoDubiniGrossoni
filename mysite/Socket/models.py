from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class SocketManager(models.Model):
    
    def create_socket(self, chargingStation, type, status):
        
        socket = Socket()
        socket.chargingStation = chargingStation
        socket.type = type
        socket.status = status
        socket.price = socket.assign_price()
        socket.save(using=self._db)
        return socket

    pass

class Socket(models.Model):

    class SocketType(models.TextChoices):
        FAST = 'F', _('Fast')
        RAPID = 'R', _('Rapid')
        SLOW = 'S', _('Slow')

    class SocketStatus(models.TextChoices):
        AVAILABLE = 'Y', _('Available')
        UNAVAILABLE = 'N', _('Unavailable')
        CHARGING = 'C', _('Charging')

    chargingStation = models.ForeignKey('ChargingStation.ChargingStation', on_delete=models.CASCADE, related_name='sockets')
    type = models.CharField(
        max_length=1,
        choices=SocketType.choices,
        default=SocketType.SLOW,
    )
    status = models.CharField(
        max_length=1,
        choices=SocketStatus.choices,
        default=SocketStatus.AVAILABLE,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2) #price is meant to be in kwh and is supposed to be a base price


    REQUIRED_FIELDS = ['chargingStation', 'type', 'status']

    def get_id(self):
        return self.id
    
    def get_availability(self):
        return self.status

    def get_type(self):
        return self.type

    def get_price(self):
        return self.price

    def is_available(self):
        return self.status == self.SocketStatus.AVAILABLE

    def is_unavailable(self):
        return self.status == self.SocketStatus.UNAVAILABLE
    
    def is_charging(self):
        return self.status == self.SocketStatus.CHARGING
    
    def assign_price(self):
        #function that assigns a price to the socket based on the type of socket, doesn't save it 
        tempPrice = 0
        if self.chargingStation.is_battery_powered():
            tempPrice = self.chargingStation.connected_bss.get_price()
        else:
            tempPrice = self.chargingStation.get_active_dso().get_price()

        if self.type == self.SocketType.FAST:
            tempPrice = 1.5 * tempPrice
        elif self.type == self.SocketType.RAPID:
            tempPrice = 1.3 * tempPrice
        elif self.type == self.SocketType.SLOW:
            tempPrice = 1.1 * tempPrice
        return tempPrice

    def update_price(self):
        #function that updates the price of the socket
        self.price = self.assign_price()
        self.save() 

    #function that if called changes the status of the socket to unavailable
    def set_unavailable(self):
        self.status = self.SocketStatus.UNAVAILABLE
        self.save()

    def set_available(self):
        self.status = self.SocketStatus.AVAILABLE
        self.save()    

    def set_charging(self):
        self.status = self.SocketStatus.CHARGING
        self.save() 