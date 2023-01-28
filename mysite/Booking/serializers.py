from django.shortcuts import render
import datetime
from rest_framework import serializers
from Booking.models import Booking, BookingManager

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id','chargingStation','socket', 'user', 'date', 'time')


class CreateBookingSerializer(serializers.ModelSerializer):
    _db = 'default'

    class Meta:
        model = Booking 
        fields = ('chargingStation','socket','user', 'date', 'time')
           

    def validate(self, attrs):
        #if attrs['date'] < datetime.date.today():
        #    raise serializers.ValidationError(
        #        {"date": "Date must be in the future.
        conflicting_bookings = Booking.objects.filter(date=attrs['date'], time=attrs['time'])
        if conflicting_bookings.exists():
            raise serializers.ValidationError(
                {"booking ":"This time slot is already booked."})

        return attrs
    
    def create(self, validated_data):
        # try to create booking, if exception is raised, return it
        try:
            booking = BookingManager.create_booking(
                self,
                validated_data['chargingStation'],
                validated_data['socket'],
                validated_data['user'],
                validated_data['date'],
                validated_data['time'],
            )
            return booking

        except Exception as e:
            error_message = e.__cause__
            print("EXEPTION", e)
            raise serializers.ValidationError({"error": str(error_message)})
