from django.shortcuts import render
import datetime
from rest_framework import serializers
from ChargingStation.models import ChargingStation, ChargingStationManager
from Socket.serializers import SocketSerializer
from Discount.serializers import DiscountSerializer
from Discount.models import Discount
from EnergyProvider.serializers import DSO_Serializer, BSS_Serializer
from Booking.serializers import BookingSerializer
# keep in mind that there won't be an actual form available for the user to add a station
# this is just for testing purposes, maybe only available to an admin

#Full Details of a Charging Station
class ChargingStationSerializer(serializers.ModelSerializer):
    sockets = SocketSerializer(many=True, read_only=True)
    connected_dsos = DSO_Serializer(many=True, read_only=True)
    connected_bss = BSS_Serializer(read_only=True)
    bookings = BookingSerializer(many=True, read_only=True)
    class Meta:
        model = ChargingStation
        fields = ('id', 'address', 'active_dso', 'sockets', 'connected_dsos', 'connected_bss', 'bookings', 'city')

#Same as above, but with less details (suitable for the EMSP)
class ChargingStationBookingsSerializer(serializers.ModelSerializer):
    bookings = BookingSerializer(many=True, read_only=True)
    sockets = SocketSerializer(many=True, read_only=True)
    class Meta:
        model = ChargingStation
        fields = ('id', 'address', 'sockets', 'bookings', 'city')

class CreateChargingStationSerializer(serializers.ModelSerializer):
    _db = 'default'

    class Meta:
        model = ChargingStation
        fields = ('address', 'connected_dsos', 'active_dso')

    def validate(self, attrs):
        if attrs['address'] == None:
            raise serializers.ValidationError(
                {"address": "You must select an address"})

        if attrs['connected_dsos'] == None:
            raise serializers.ValidationError(
                {"connected_dsos": "You must select at least one DSO"})
        
        if attrs['active_dso'] == None:
            raise serializers.ValidationError(
                {"active_dso": "You must select an active DSO"})

        if attrs['active_dso'] not in attrs['connected_dsos']:
            raise serializers.ValidationError(
                {"active_dso": "The active DSO must be one of the connected DSOs"})
        
        return attrs
    
    def create(self, validated_data):
        try:
            station = ChargingStationManager.create_station(
                self,
                validated_data['address'],
                validated_data['connected_dsos'],
                validated_data['active_dso'],
                validated_data['city']
            )
            return station
            
        except Exception as e:
            error_message = e.__cause__
            print("EXEPTION", e)
            raise serializers.ValidationError({"error": str(error_message)})

# create a class