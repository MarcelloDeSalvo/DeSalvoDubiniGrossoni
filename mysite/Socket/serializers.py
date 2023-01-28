from django.shortcuts import render
import datetime
from rest_framework import serializers
from Socket.models import Socket, SocketManager

class SocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socket
        fields = ('id','chargingStation', 'type', 'status', 'price')

class CreateSocketSerializer(serializers.ModelSerializer):
    _db = 'default'

    class Meta:
        model = Socket
        fields = ('chargingStation', 'type', 'status', 'price')
        extra_kwargs = {
            'chargingStation' : {'required' : True},
            'type': {'required': True},
            'status': {'required': True},
            'price': {'required': True},
        }

    def validate(self, attrs):
        if attrs['chargingStation'] == None:
            raise serializers.ValidationError(
                {"chargingStation": "You must select a charging station"})
        if attrs['type'] == None:
            raise serializers.ValidationError(
                {"type": "You must select a socket type"})
        if attrs['status'] == None:
            raise serializers.ValidationError(
                {"status": "You must select a socket status"})
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
            socket = SocketManager.create_socket(
                self,
                validated_data['chargingStation'],
                validated_data['type'],
                validated_data['status'],
                validated_data['price'],
            )
            return socket
        except Exception as e:
            error_message = e.__cause__
            print("EXEPTION", e)
            raise serializers.ValidationError({"error": str(error_message)})