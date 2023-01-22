from django.shortcuts import render
import datetime
from rest_framework import serializers
from Discount.models import Discount, DiscountManager

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('id', 'start_date','end_date','discount_amount','applied_stations')

class CreateDiscountSerializer(serializers.ModelSerializer):
    _db = 'default'

    class Meta:
        model = Discount
        fields = ('start_date','end_date','discount_amount','applied_stations')
        extra_kwargs = {
            'start_date' : {'required' : True},
            'end_date': {'required': True},
            'discount_amount': {'required': True},
            'applied_stations': {'required': True},
        }

    def validate(self, attrs):
        if attrs['start_date'] > attrs['end_date']:
            raise serializers.ValidationError(
                {"start_date": "Start date must be before end_date"})

        if attrs['discount_amount']==0:
            raise serializers.ValidationError(
                {"discount_amount": "You can't apply a 0 discount"})

        if attrs['start_date'] < datetime.date.today():
            raise serializers.ValidationError(
                {"start_date": "You can't apply a discount in the past"})

        if attrs['end_date'] < datetime.date.today():
            raise serializers.ValidationError(
                {"end_date": "You can't end a discount in the past"})
        
        if attrs['start_date'] == attrs['end_date']:
            raise serializers.ValidationError(
                {"end_date": "You can't end a discount in the same day it starts"})

        if attrs['discount_amount'] < 0:
            raise serializers.ValidationError(
                {"discount_amount": "You can't apply a negative discount"})

        if attrs['discount_amount'] >= 100:
            raise serializers.ValidationError(
                {"discount_amount": "You can't apply a discount higher than 100%"})
        
        if attrs['applied_stations'] == None:
            raise serializers.ValidationError(
                {"applied_stations": "You must select at least one charging station"})
                
        return attrs


    def create(self, validated_data):
        # try to create the discount, if exception is raised, return it
        try:
            discount = DiscountManager.create_discount(
                self,
                validated_data['start_date'],
                validated_data['end_date'],
                validated_data['discount_amount'],
                validated_data['applied_stations'],
            )
            return discount

        except Exception as e:
            error_message = e.__cause__
            print("EXEPTION", e)
            raise serializers.ValidationError({"error": str(error_message)})

class DeleteDiscountSerializer(serializers.ModelSerializer):
    _db = 'default'

    class Meta:
        model = Discount
        fields = ('id',)

    def validate(self, attrs):
        if attrs['id'] == None:
            raise serializers.ValidationError(
                {"id": "You must select a discount to delete"})
        return attrs

    def delete(self, validated_data):
        # try to delete the discount, if exception is raised, return it
        try:
            discount = DiscountManager.delete_discount(
                self,
                validated_data['id'],
            )
            return discount

        except Exception as e:
            error_message = e.__cause__
            print("EXEPTION", e)
            raise serializers.ValidationError({"error": str(error_message)})