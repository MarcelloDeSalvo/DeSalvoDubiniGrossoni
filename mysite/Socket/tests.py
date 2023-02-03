from django.test import TestCase, Client

from ChargingStation.models import ChargingStation, ChargingStationManager
from rest_framework_simplejwt.authentication import JWTAuthentication
from EnergyProvider.models import  DSO, DSOManager, BSS, BSSManager
from Socket.models import Socket, SocketManager

class TestSocket(TestCase):

    def setUp(self):
        dsoManag=DSOManager()
        chargingManager=ChargingStationManager()
        socketManager=SocketManager()
        dsoManag.create_dso(name="DSO1", availability=True, price="1.0")
        chargingManager.create_station(address='Via Roma 1', connected_dsos=[DSO.objects.get(name='DSO1')], active_dso=DSO.objects.get(name='DSO1'))
        socketManager.create_socket(chargingStation=ChargingStation.objects.get(address='Via Roma 1'), type='S', status="Y")
        socket=Socket.objects.filter(type='S', status="Y", chargingStation=ChargingStation.objects.get(address='Via Roma 1')).first()
        socket.set_email("mail@mail.it") #hard set email as if the socket was connected to a car
        socket.save()

    def test_create_socket_correctly(self):
        socket=SocketManager()
        chargingStation=ChargingStation.objects.get(address='Via Roma 1')
        socket=socket.get_socket_by_id(chargingStation.get_sockets()[0].get_id())
        self.assertEqual(socket.get_type(), 'S')
        self.assertEqual(socket.get_status(), 'Y')
        self.assertEqual(socket.get_station().get_address(), 'Via Roma 1')

    def test_get_socket_by_id(self):
        socket=Socket.objects.filter(type='S', status="Y", chargingStation=ChargingStation.objects.get(address='Via Roma 1')).first()
        response=self.client.post('/OCPI/getSocket/' + str(socket.get_id()) + '/', {"email": "mail@mail.it"})
        responseSocket=response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(responseSocket["type"], 'S')
        self.assertEqual(responseSocket["status"], 'Y')

        self.assertEqual(responseSocket["chargingStation"], socket.get_station().get_id())

    def test_reset_socket(self):
        socket=Socket.objects.filter(type='S', status="Y", chargingStation=ChargingStation.objects.get(address='Via Roma 1')).first()
        socket.set_charging()
        self.assertEqual(socket.get_status(), 'C')
        response=self.client.get('/OCPI/resetSocket/' + str(socket.get_id()) + '/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(socket.get_status(), 'Y')


    #this next test works fine, but the creation of an additional thread that changes one of the socket's variable causes problems with the deletion of the mock database
    #the test results is OK, but the database deletion causes an error

    #def test_startCharge(self):
    #    socket=Socket.objects.filter(type='S', status="Y", chargingStation=ChargingStation.objects.get(address='Via Roma 1')).first()
    #    socket.remove_email()
    #    socket.set_available()
    #    response=self.client.post('/OCPI/startCharge', {"email": "mail@mail.it", "socket" : socket.get_id()})
    #    self.assertEqual(response.json()["socket"], str(socket.get_id()))
    #    self.assertEqual(response.status_code, 200)
        

        