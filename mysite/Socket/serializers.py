from django.shortcuts import render
import datetime
from rest_framework import serializers
from Socket.models import Socket, SocketManager

class SocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socket
        fields = ('id','chargingStation', 'socketType', 'socketStatus', 'price')

class CreateBookingSerializer(serializers.ModelSerializer):
    _db = 'default'

    class Meta:
        model = Socket
        fields = ('chargingStation', 'socketType', 'socketStatus', 'price')
        extra_kwargs = {
            'chargingStation' : {'required' : True},
            'socketType': {'required': True},
            'socketStatus': {'required': True},
            'price': {'required': True},
        }

    def validate(self, attrs):
        if attrs['chargingStation'] == None:
            raise serializers.ValidationError(
                {"chargingStation": "You must select a charging station"})
        if attrs['socketType'] == None:
            raise serializers.ValidationError(
                {"socketType": "You must select a socket type"})
        if attrs['socketStatus'] == None:
            raise serializers.ValidationError(
                {"socketStatus": "You must select a socket status"})
        if attrs['price'] <0:
            raise serializers.ValidationError(
                {"price": "You can't have a negative price"})
        if attrs['price'] == None:
            raise serializers.ValidationError(
                {"price": "You must select a price"})
        return attrs
    
    def create(self, validated_data):
        # try to create user, if exception is raised, return it
        try:
            booking = SocketManager.create_booking(
                self,
                validated_data['chargingStation'],
                validated_data['socketType'],
                validated_data['socketStatus'],
                validated_data['price'],
            )
            return booking
        except Exception as e:
            error_message = e.__cause__
            print("EXEPTION", e)
            raise serializers.ValidationError({"error": str(error_message)})