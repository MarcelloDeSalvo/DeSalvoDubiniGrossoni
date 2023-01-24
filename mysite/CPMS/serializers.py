from django.shortcuts import render
import datetime
from rest_framework import serializers
from .models import CPMS, CPMSManager


from Booking.serializers import BookingSerializer
# keep in mind that there won't be an actual form available for the user to add a station
# this is just for testing purposes, maybe only available to an admin

#Full Details of a Charging Station
class CPMSSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = CPMS
        fields = ('id', 'name', 'url')



class CreateCPMSSerializer(serializers.ModelSerializer):
    _db = 'default'

    class Meta:
        model = CPMS
        fields = ('name', 'url')
        extra_kwargs = {
            'name': {'required': True},
            'url': {'required': True},
        }

    def validate(self, attrs):
        if attrs['name'] == None:
            raise serializers.ValidationError(
                {"name": "Name is required."})
        if attrs['url'] == None:
            raise serializers.ValidationError(
                {"url": "url is required."})
        return attrs
    
    def create(self, validated_data):
        try:
            cpms = CPMSManager.create_cpms(
                self,
                validated_data['name'],
                validated_data['url']
            )
            return cpms
            
        except Exception as e:
            error_message = e.__cause__
            print("EXEPTION", e)
            raise serializers.ValidationError({"error": str(error_message)})