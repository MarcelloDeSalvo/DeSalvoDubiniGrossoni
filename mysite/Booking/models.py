from django.db import models

class BookingManager(models.Model):

    def create_booking(self, chargingStation, socket, user, date, time):
        booking = Booking()
        booking.chargingStation = chargingStation
        booking.socket = socket
        booking.user = user
        booking.date = date
        booking.time = time       
        booking.save(using=self._db)
        return booking
    
    def get_booking_by_id(self, id):
        return self.get(id=id)
    
    
    pass

# Create your models here.
class Booking(models.Model):

    # set fields for a date, a time, a stationID, a userID, a socketID
    chargingStation = models.ForeignKey('ChargingStation.ChargingStation', 
        on_delete=models.CASCADE, 
        related_name='bookings', 
        default=None)
    socket = models.ForeignKey('Socket.Socket', 
        on_delete=models.CASCADE, 
        related_name='bookingSocket')
    user = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=False,
        default=None
    )
    date = models.DateField(default=None)
    time = models.TimeField(default=None)
    objects = BookingManager()
    

    REQUIRED_FIELDS = ['chargingStation','socket','user', 'date', 'time']

    def get_id(self):
        return self.id
    
    def get_user(self):
        return self.user

    def get_date(self):
        return self.date
    
    def get_time(self):
        return self.time

    def get_chargingStation(self):
        return self.chargingStation
    
    def get_socket(self):
        return self.socket
    
    

   # def __str__(self):
    #    return "Booking: " + str(self.id) + " - " + str(self.user) + " - " + str(self.date) + " - " + str(self.time)

