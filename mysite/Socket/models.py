from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class SocketManager(models.Model):
    pass

class Socket(models.Model):

    class SocketType(models.TextChoices):
        FAST = 'F', _('Fast')
        RAPID = 'R', _('Rapid')
        SLOW = 'S', _('Slow')

    class SocketStatus(models.TextChoices):
        AVAILABLE = 'Y', _('Available')
        UNAVAILABLE = 'N', _('UNAVAILABLE')

    chargingStation = models.ForeignKey('ChargingStation.ChargingStation', on_delete=models.CASCADE, related_name='sockets')
    socketType = models.CharField(
        max_length=1,
        choices=SocketType.choices,
        default=SocketType.SLOW,
    )
    socketStatus = models.CharField(
        max_length=1,
        choices=SocketStatus.choices,
        default=SocketStatus.AVAILABLE,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)


    REQUIRED_FIELDS = ['chargingStation', 'socketType', 'socketStatus', 'price']

    def get_id(self):
        return self.id
    
    def get_availability(self):
        return self.socketStatus

    def get_type(self):
        return self.socketType

    def get_price(self):
        return self.price


    def __str__(self):
       return 