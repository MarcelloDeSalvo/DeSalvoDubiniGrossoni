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
        socket.connectedUserEmail = None
        socket.save()
        return socket

    def get_socket_by_id(self, id):
        return self.get(id=id)

    def filter(self, **kwargs):
        return Socket.objects.filter(**kwargs)
    def get(self, **kwargs):
        return Socket.objects.get(**kwargs)

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
    connectedUserEmail = models.CharField(max_length=255, null=True, blank=True) 


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

    def get_charging_station(self):
        return self.chargingStation
    
    def get_email(self):
        return self.connectedUserEmail
    
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

    def set_email(self, email):
        self.connectedUserEmail = email
        self.save()

    def remove_email(self):
        self.connectedUserEmail = None
        self.save()

    def get_status(self):
        return self.status

    def get_station(self):
        return self.chargingStation