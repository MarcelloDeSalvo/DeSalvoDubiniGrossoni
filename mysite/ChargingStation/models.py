from django.db import models

# Create your models here.
class ChargingStationManager(models.Model):
    def create_station(self, address, connected_dsos, active_dso):
        
        station = ChargingStation()
        station.address = address
        station.active_dso = active_dso
        station.save(using=self._db)
        station.connected_dsos.set(connected_dsos)
        return station
    
    def get_station_by_id(self, id):
        return self.get(id=id)

    def get_sockets(self, id):
        return self.get(id=id).sockets.all()
    
    pass

class ChargingStation(models.Model):
 
    address = models.CharField(max_length=255, default=None, unique=True)
    connected_dsos = models.ManyToManyField('EnergyProvider.DSO',related_name='connected_dsos')
    active_dso = models.ForeignKey('EnergyProvider.DSO', on_delete=models.DO_NOTHING, related_name='active_dso', default=None)
    
    objects = ChargingStationManager()
    

    REQUIRED_FIELDS = ['address', 'connected_dsos', 'active_dso']

    def get_id(self):
        return self.id
    
    def get_sockets(self):
        return self.sockets.all()

    def get_bookings(self):
        return self.bookings.all()

    def get_active_dso(self):
        return self.active_dso

    def is_battery_powered(self):
        return self.connected_bss.isActive

    def update_prices(self):
        #function that updates the prices of all the sockets
        for socket in self.sockets.all():
            socket.assign_price()
