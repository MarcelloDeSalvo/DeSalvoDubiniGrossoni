from django.db import models

class BookingManager(models.Model):
    pass

# Create your models here.
class Booking(models.Model):
    # prova 123
    service = BookingManager()

    start_time = models.DateTimeField()
    

    REQUIRED_FIELDS = ['start_time']  # Email & Password are required by default.
