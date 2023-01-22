from django.shortcuts import render
import datetime
from rest_framework import serializers
from ChargingStation.models import ChargingStation, ChargingStationManager

# keep in mind that there won't be an actual form available for the user to add a station
# this is just for testing purposes, maybe only available to an admin
class ChargingStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargingStation
        fields = ('id', 'address')

class CreateChargingStationSerializer(serializers.ModelSerializer):
    _db = 'default'

    class Meta:
        model = ChargingStation
        fields = ('address',)
        extra_kwargs = {
            'address' : {'required' : True},
        }

    def validate(self, attrs):
        if attrs['address'] == None:
            raise serializers.ValidationError(
                {"address": "You must select an address"})
        return attrs
    
    def create(self, validated_data):
        try:
            station = ChargingStationManager.create_station(
                self,
                validated_data['address']
            )
            return station
            
        except Exception as e:
            error_message = e.__cause__
            print("EXEPTION", e)
            raise serializers.ValidationError({"error": str(error_message)})