from django.shortcuts import render
import datetime
from rest_framework import serializers
from Discount.models import Discount, DiscountManager

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('start_date','end_date','discount_amount')

class CreateDiscountSerializer(serializers.ModelSerializer):
    _db = 'default'

    class Meta:
        model = Discount
        fields = ('start_date','end_date','discount_amount')
        extra_kwargs = {
            'start_date' : {'required' : True},
            'end_date': {'required': True},
            'discount_amount': {'required': True},
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
        

        return attrs


    def create(self, validated_data):
        # try to create the discount, if exception is raised, return it
        try:
            discount = DiscountManager.create_discount(
                self,
                validated_data['start_date'],
                validated_data['end_date'],
                validated_data['discount_amount'],
            )
            return discount

        except Exception as e:
            error_message = e.__cause__
            print("EXEPTION", e)
            raise serializers.ValidationError({"error": str(error_message)})