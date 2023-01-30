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
 
    city = models.CharField(max_length=255, default="Milan")
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

    def get_battery(self):
        if not hasattr(self,"connected_bss"):
            return None
        return self.connected_bss

    def is_battery_powered(self):
        if(not hasattr(self,"connected_bss")):
            return False
        return self.connected_bss.isActive

    def update_prices(self):
        #function that updates the prices of all the sockets
        for socket in self.sockets.all():
            socket.update_price()

    def select_best_provider_auto(self):
        #function that selects the best provider for the station
        #ideally this would be called periodically by a periodic task in the background

        #if the station is not battery powered, the best provider is the cheapest DSO
        #if the station is battery powered, the best provider is the BSS if it is available and has energy and cost less than the cheapest DSO
    
        #select the DSO with the lowest price
        connected_dsos_list = self.connected_dsos.all()
        best_dso = connected_dsos_list[0]
        for dso in connected_dsos_list:
            if(dso.price < best_dso.price):
                best_dso = dso
        #switch the active DSO to the best DSO
        self.active_dso = best_dso

        battery = self.get_battery()
        if(battery is not None):
            if(battery.availability and battery.currentEnergy > 0):
                if(battery.price < best_dso.price):
                    battery.isActive = True
                    battery.save()
                else:
                    battery.isActive = False
                    battery.save()
            else:
                battery.isActive = False
                battery.save()

        # save the station and update the prices of all the sockets
        self.save()
        self.update_prices()
        

          
