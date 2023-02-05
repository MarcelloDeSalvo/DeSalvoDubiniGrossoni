from django.utils import timezone
from django.core.management.base import BaseCommand
from Discount.models import Discount

class Command(BaseCommand):
    help = 'Checks for active discounts each day'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        print("WE IN")
        activating_discounts = Discount.objects.filter(start_date=today)
        for discount in activating_discounts:
            #check if discount is expired
            if discount.end_date < today:
                discount.active = False
                discount.save()
                print("Discount expired")   

            # Activate the discounts and delete the ones that are replaced    
            #Se 
            



