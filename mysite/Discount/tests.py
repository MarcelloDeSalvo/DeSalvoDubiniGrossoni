from django.test import TestCase

from ChargingStation.models import ChargingStation, ChargingStationManager
from rest_framework_simplejwt.authentication import JWTAuthentication
from EnergyProvider.models import  DSO, DSOManager, BSS, BSSManager
from Socket.models import Socket, SocketManager
from Discount.models import Discount, DiscountManager

# Create your tests here.
class TestDiscount(TestCase):

    def setUp(self):
        Dsocool=DSOManager()
        chargingManager=ChargingStationManager()
        socketManager=SocketManager()
        discountManager=DiscountManager()
        Dsocool.create_dso(name="DSO1", availability=True, price="1.0")
        chargingManager.create_station(address='Via Roma 1', connected_dsos=[DSO.objects.get(name='DSO1')], active_dso=DSO.objects.get(name='DSO1'))
        socketManager.create_socket(chargingStation=ChargingStation.objects.get(address='Via Roma 1'), type='S', status="Y")
        socket=Socket.objects.filter(type='S', status="Y", chargingStation=ChargingStation.objects.get(address='Via Roma 1')).first()
        socket.set_email("mail@mail.it") #hard set email as if the socket was connected to a car
        socket.save()
        discountManager.create_discount(start_date="2023-01-01", end_date="2023-01-05", discount_amount=20, applied_stations=[ChargingStation.objects.get(address='Via Roma 1')])

    def test_create_discount_correctly(self):
        discount=Discount.objects.filter(start_date="2023-01-01", end_date="2023-01-05", discount_amount=20, applied_stations=ChargingStation.objects.get(address='Via Roma 1').get_id()).first()
        self.assertEqual(str(discount.get_start_date()), "2023-01-01")
        self.assertEqual(str(discount.get_end_date()), "2023-01-05")
        self.assertEqual(discount.get_discount_amount(), 20)
        self.assertEqual(discount.get_applied_stations().first().get_address(), 'Via Roma 1')

    def test_delete_discount_correctly(self):
        number_of_discounts1=Discount.objects.all().count()
        discount=DiscountManager()
        discount.delete_discount(Discount.objects.filter(start_date="2023-01-01", end_date="2023-01-05", discount_amount=20, applied_stations=ChargingStation.objects.get(address='Via Roma 1').get_id()).first())
        number_of_discounts2=Discount.objects.all().count()
        self.assertEqual(number_of_discounts1, number_of_discounts2+1)

    def test_get_discount(self):
        chargingStation=ChargingStationManager()
        chargingStation=chargingStation.get_station_by_id(ChargingStation.objects.get(address='Via Roma 1').get_id())
        response=self.client.get('/OCPI/requestChargingStationById/' + str(ChargingStation.objects.get(address='Via Roma 1').get_id()) + '/')
        self.assertEqual(response.status_code, 200)
        discount=response.json()
        discount=discount['discounts']
        #since the station was created only in this test, and the discount is the only applied to it, the discount is the only one in the list, so we can access it with [0]
        #we check that the discount is the one we created
        self.assertEqual(discount[0]['start_date'], "2023-01-01")
        self.assertEqual(discount[0]['end_date'], "2023-01-05")
        self.assertEqual(discount[0]['discount_amount'], 20)

        
        
        
