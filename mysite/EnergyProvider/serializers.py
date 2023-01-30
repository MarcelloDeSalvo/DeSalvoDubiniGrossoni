from django.shortcuts import render
from rest_framework import serializers
from EnergyProvider.models import DSO, BSS, EnergyProviderInterface, EnergyProviderManager, DSOManager, BSSManager
from ChargingStation.models import ChargingStation

from rest_framework import serializers

class DSO_Serializer(serializers.ModelSerializer):
    class Meta:
        model = DSO
        fields = ('id', 'name', 'availability', 'price')

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
        fields = ('name', 'availability', 'price')

    def validate(self, attrs):
            
            if attrs['price'] < 0:
                raise serializers.ValidationError("Price cannot be negative")
                
            return attrs

    def create(self, validated_data):
        try :
            return DSO.objects.create(**validated_data)
        except:
            raise serializers.ValidationError("Error creating DSO")

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
        try :
            return BSS.objects.create(**validated_data)
        except:
            raise serializers.ValidationError("Error creating BSS")


class ToggleBSSSerializer(BSS_Serializer):
    # Switches between active and inactive state
    class Meta:
        model = BSS
        fields = ('id',)

    def validate(self, attrs):
        return attrs
        
    def update(self, instance, validated_data):
        try :
            newStatus = not instance.isActive
            if newStatus == True and instance.availability == False:
                raise serializers.ValidationError("Cannot activate a provider that is not available")

            instance.isActive = not instance.isActive
            instance.station.update_prices()
            instance.save()
            return instance
        except:
            raise serializers.ValidationError("Error finding BSS")


class SwitchDSOSerializer(serializers.ModelSerializer):
    # Change current DSO on the Charging Station
    class Meta:
        model = ChargingStation
        fields = ('active_dso',)

    def validate(self, attrs):
        connectedDsoIds = [dso.id for dso in self.instance.connected_dsos.all()]
        if attrs['active_dso'].id not in connectedDsoIds:
            raise serializers.ValidationError("DSO not connected to the station")

        if attrs['active_dso'].id == self.instance.active_dso.id:
            raise serializers.ValidationError("DSO already active")
        
        if attrs['active_dso'].availability == False:
            raise serializers.ValidationError("DSO not available")
        
        return attrs

    def update(self, instance, validated_data):
        try :
            instance.active_dso = validated_data['active_dso']
            instance.save()
            instance.update_prices()
            return instance
        except:
            raise serializers.ValidationError("Error finding DSO")


