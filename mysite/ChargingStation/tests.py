from django.test import TestCase, Client

from .models import ChargingStation, ChargingStationManager
from rest_framework_simplejwt.authentication import JWTAuthentication
from EnergyProvider.models import  DSO, DSOManager, BSS, BSSManager
from Socket.models import Socket, SocketManager

class TestChargingStations(TestCase):

    def setUp(self):
        Dsocool=DSOManager()
        chargingManager=ChargingStationManager()
        socketManager=SocketManager()
        
        Dsocool.create_dso(
             name="DSO1", availability=True, price="1.0")
        
        chargingManager.create_station(address='Via Roma 1', connected_dsos=[DSO.objects.get(name='DSO1')], active_dso=DSO.objects.get(name='DSO1'))
        
        socketManager.create_socket(chargingStation=ChargingStation.objects.get(address='Via Roma 1'), type='S', status="Y")

        # checks if the station is created and saved correctly
    def test_get_station_by_id(self):
        chargingStation=ChargingStationManager()
        chargingStation=chargingStation.get_station_by_address(address='Via Roma 1')
        self.assertEqual(chargingStation.get_address(), 'Via Roma 1')
        self.assertEqual(chargingStation.get_active_dso().get_name(), 'DSO1')
        self.assertEqual(chargingStation.get_sockets()[0].get_type(), 'S')
        self.assertEqual(chargingStation.get_sockets()[0].get_status(), 'Y')
        self.assertEqual(chargingStation.get_sockets()[0].get_station().get_address(), 'Via Roma 1')

        # test if the get_station_by_id api works. 
    def test_check_get_station_check(self):
        chargingStation=ChargingStationManager()
        chargingStation=chargingStation.get_station_by_id(id=1)
        response=self.client.get('/OCPI/requestChargingStationById/' + '1' + '/')
        self.assertEqual(response.status_code, 200)
        station=response.json()
        station=station['station']
        self.assertEqual(station['address'], chargingStation.get_address())
        self.assertEqual(len(station['sockets']), len(chargingStation.get_sockets()))
        self.assertEqual(station['sockets'][0]['type'], chargingStation.get_sockets()[0].get_type())

        # checks if the get_all_stations api works, checks if all the stations are returned.
    def test_get_all_stations(self):
        chargingStations=ChargingStation.objects.all()
        response=self.client.get('/OCPI/getChargingStations')
        self.assertEqual(response.status_code, 200)
        stations=response.json()
        self.assertEqual(len(stations), len(chargingStations))
        
        
