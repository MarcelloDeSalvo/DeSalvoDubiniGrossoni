from django.shortcuts import render
from rest_framework import serializers
from EnergyProvider.models import DSO, BSS, EnergyProviderInterface, EnergyProviderManager, DSOManager, BSSManager

from rest_framework import serializers

class DSO_Serializer(serializers.ModelSerializer):
    class Meta:
        model = DSO
        fields = ('id', 'station', 'name', 'availability', 'price')

class BSS_Serializer(serializers.ModelSerializer):
    class Meta:
        model = BSS
        fields = ('id', 'station', 'name', 'availability', 'price', 'capacity', 'currentEnergy', 'isActive')

class EnergyProviderInterface_Serializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyProviderInterface
        fields = ('name', 'availability', 'price')


class RegisterDSOSerializer(DSO_Serializer):
    class Meta:
        model = DSO
        fields = ('station', 'name', 'availability', 'price')

    def validate(self, attrs):
            
            if attrs['price'] < 0:
                raise serializers.ValidationError("Price cannot be negative")
                
            return attrs

    def create(self, validated_data):
        return DSO.objects.create_dso(**validated_data)

class RegisterBSSSerializer(BSS_Serializer):
    class Meta:
        model = BSS
        fields = ('station', 'name', 'availability', 'price', 'capacity', 'currentEnergy', 'isActive')

    def validate(self, attrs):

        if attrs['capacity'] < attrs['currentEnergy']:
            raise serializers.ValidationError("Current energy cannot be greater than capacity")

        if attrs['capacity'] < 0:
            raise serializers.ValidationError("Capacity cannot be negative")

        if attrs['currentEnergy'] < 0:
            raise serializers.ValidationError("Current energy cannot be negative")

        if attrs['price'] < 0:
            raise serializers.ValidationError("Price cannot be negative")

        if attrs['isActive'] == True and attrs['availability'] == False:
            raise serializers.ValidationError("Cannot activate a provider that is not available")
        
        
        return attrs

    def create(self, validated_data):
        return BSS.objects.create(**validated_data)