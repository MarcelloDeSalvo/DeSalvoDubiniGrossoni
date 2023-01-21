from django.db import models

# Create your models here.
class ChargingStationManager(models.Model):
    def create_station(self, address):
        #print("data in create booking", user, date, time, stationID, socketID, cpmsID)
        station = ChargingStation()
        station.address = address
        station.save(using=self._db)
        return station
    
    def get_station_by_id(self, id):
        return self.get(id=id)
    
    pass

class ChargingStation(models.Model):
 
    address = models.CharField(max_length=255, default=None)
    objects = ChargingStationManager()
    

    REQUIRED_FIELDS = ['address']

    def get_id(self):
        return self.id
    
    def get_sockets(self):
        return self.sockets.all()

    def get_bookings(self):
        return self.bookings.all()
