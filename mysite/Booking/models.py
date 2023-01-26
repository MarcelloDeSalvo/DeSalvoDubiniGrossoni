from django.db import models

class BookingManager(models.Model):

    def create_booking(self, user, date, time, stationID, socketID, cpmsID, stationAddress):
        #print("data in create booking", user, date, time, stationID, socketID, cpmsID)
        booking = Booking()
        booking.user = user
        booking.date = date
        booking.time = time
        booking.stationID = stationID
        booking.socketID = socketID
        booking.cpmsID = cpmsID 
        booking.stationAddress = stationAddress
        booking.save(using=self._db)
        return booking
    
    def get_booking_by_id(self, id):
        return self.get(id=id)
    
    def get_bookings_by_userID(self, userID):
        return self.filter(userID=userID)
    
    def get_bookings_by_cpmsID(self, cpmsID):
        return self.filter(cpmsID=cpmsID)
    
    pass

# Create your models here.
class Booking(models.Model):

    # set fields for a date, a time, a stationID, a userID, a socketID
    user = models.ForeignKey('User.User', on_delete=models.CASCADE, default=None)
    date = models.DateField(default=None)
    time = models.TimeField(default=None)
    stationID = models.CharField(max_length=20, default=None)
    stationAddress = models.CharField(max_length=100, default=None)
    socketID = models.CharField(max_length=20, default=None)
    cpmsID = models.CharField(max_length=20, default=None)
    objects = BookingManager()
    

    REQUIRED_FIELDS = ['user', 'date', 'time', 'stationID', 'socketID', 'cpmsID', 'stationAddress']

    def get_id(self):
        return self.id
    
    def get_user(self):
        return self.user

    def get_date(self):
        return self.date
    
    def get_time(self):
        return self.time

    def get_stationID(self):
        return self.stationID

    def get_socketID(self):
        return self.socketID

    def get_cpmsID(self):
        return self.cpmsID

    def get_stationAddress(self):
        return self.stationAddress

    def __str__(self):
        return "Booking: " + str(self.id) + " - " + str(self.date) + " - " + str(self.time) + " - " + str(self.stationID) + " - " + str(self.user) + " - " + str(self.socketID + " - " + str(self.stationAddress))

    
