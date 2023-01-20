import datetime
from rest_framework import serializers
from Booking.models import Booking, BookingManager

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'user', 'date', 'time', 'stationID', 'socketID', 'cpmsID')

class CreateBookingSerializer(serializers.ModelSerializer):
    _db = 'default'

    class Meta:
        model = Booking
        fields = ('user', 'date', 'time', 'stationID', 'socketID', 'cpmsID')
        extra_kwargs = {
            'user': {'required': True},
            'date': {'required': True},
            'time': {'required': True},
            'stationID': {'required': True},
            'socketID': {'required': True},
            'cpmsID': {'required': True}
        }

    def validate(self, attrs):
        if attrs['date'] < datetime.date.today():
            raise serializers.ValidationError(
                {"date": "Date must be in the future."})
        return attrs
    
    def create(self, validated_data):
        # try to create user, if exception is raised, return it
        try:
            booking = BookingManager.create_booking(
                self,
                validated_data['user'],
                validated_data['date'],
                validated_data['time'],
                validated_data['stationID'],
                validated_data['socketID'],
                validated_data['cpmsID']
            )
            return booking
        except Exception as e:
            error_message = e.__cause__
            print("EXEPTION", e)
            raise serializers.ValidationError({"error": str(error_message)})