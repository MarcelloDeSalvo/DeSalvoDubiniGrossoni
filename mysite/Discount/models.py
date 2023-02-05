from django.db import models

from ChargingStation.models import ChargingStation

class DiscountManager(models.Model):

    def create_discount(self, start_date, end_date, discount_amount,applied_stations):
        if not start_date:
            raise ValueError('The discount must have a start date')
        if not end_date:
            raise ValueError('The discount must have an end date')   
        if not discount_amount:
            raise ValueError('The discount must have a value that it applies') 
        

        discount = Discount()         
        discount.start_date=start_date
        discount.end_date=end_date
        discount.discount_amount=discount_amount
        discount.save()
        discount.applied_stations.set(applied_stations)
        return discount

    def delete_discount(self, discount):
        discount.delete()
        return discount
    
    def get_discout_by_id(self, id):
        return Discount.objects.get(id=id)

    def filter(self, **kwargs):
        return Discount.objects.filter(**kwargs)
    def get(self, **kwargs):
        return Discount.objects.get(**kwargs)


    pass
        

# Create your models here.
class Discount(models.Model):
    
    objects = DiscountManager()

    applied_stations = models.ManyToManyField(ChargingStation,
        related_name='applied_stations', 
        )
    start_date = models.DateField(default=None)
    end_date = models.DateField(default=None)
    discount_amount = models.IntegerField(default=10)

    REQUIRED_FIELDS = ['start_date','end_date', 'discount_amount', 'applied_stations'] #Every field is required for the discount to be registered.

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_discount_amount(self):
        return self.discount_amount

    def get_applied_stations(self):
        return self.applied_stations

    def get_id(self):
        return self.id




    
