from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class SocketManager(models.Model):
    
    def create_socket(self, chargingStation, type, status, price):
        
        socket = Socket()
        socket.chargingStation = chargingStation
        socket.type = type
        socket.status = status
        socket.price = price
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
    price = models.DecimalField(max_digits=10, decimal_places=2)


    REQUIRED_FIELDS = ['chargingStation', 'type', 'status', 'price']

    def get_id(self):
        return self.id
    
    def get_availability(self):
        return self.status

    def get_type(self):
        return self.type

    def get_price(self):
        return self.price

    #function that if called changes the status of the socket to unavailable
    def set_unavailable(self):
        self.status = self.SocketStatus.UNAVAILABLE
        self.save()

    def set_available(self):
        self.status = self.SocketStatus.AVAILABLE
        self.save()    
