from django.utils import timezone
from django.core.management.base import BaseCommand
from Discount.models import Discount

class Command(BaseCommand):
    help = 'Checks for active discounts each day'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        activating_discounts = Discount.objects.filter(start_date=now)
        for discount in activating_discounts:
            # Perform action for active discount
            print("Discount {discount.id} needs activation")