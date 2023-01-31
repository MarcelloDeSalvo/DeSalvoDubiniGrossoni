from threading import Timer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes
from ChargingStation.models import ChargingStation
from Socket.models import Socket
from Socket.serializers import SocketSerializer
from Booking.models import Booking
from ChargingStation.views import getChargingStations
from ChargingStation.serializers import ChargingStationSerializer, ChargingStationBookingsSerializer
import requests
from datetime import datetime, timedelta
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
# Create your views here.

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def requestChargingStations(request):
    stations = ChargingStation.objects.all()
    serializer = ChargingStationBookingsSerializer(stations, many=True)
    
    if stations==None:
        return Response("there are no stations", status=200)
    print("OCPI sendStations here")
    #return serializer.data in a response format
    return  Response(serializer.data, status=200)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def requestChargingStationById(request, pk):
    stations = ChargingStation.objects.filter(id=pk).first()
    serializer = ChargingStationBookingsSerializer(stations)
    
    if stations==None:
        return Response("there are no stations", status=200)
    print("OCPI sendStations here")
    #return serializer.data in a response format
    return  Response(serializer.data, status=200)
   


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def startChargeFromBooking(request):
    #initialize response
    chargeStatus=""
    #load booking
    reservation = Booking.objects.filter(time=request.data['time'], date=request.data['date'], user=request.data['email'], chargingStation=request.data['chargingStation'], socket=request.data['socket']).first()
    #check if the booking exists
    if(reservation==None):
        chargeStatus="Booking does not exist"
        return Response(chargeStatus, status=400)

    #get the booking details
    date = reservation.get_date()
    time = reservation.get_time()
    
    #load socket
    socket=Socket.objects.filter(id=request.data['socket']).first()

    #find the time difference
    bookingDateTime = datetime.combine(date, time)
    currentDateTime = datetime.now()
    timeDifference= abs(bookingDateTime - currentDateTime)
    #check if the booking starting time has arrived
    if(currentDateTime>bookingDateTime):    
        #check if the socket is available and if the booking is not expired
        if ( timeDifference<=timedelta(minutes=15) and socket.is_available()):
            socket.set_charging()
            chargeStatus="Charge Started"
            message = {
                "chargingStation": request.data['chargingStation'],
                "socket": request.data['socket'],
                "user": request.data['email'],
                "date": request.data['date'],
                "time": request.data['time'],
                "status": chargeStatus
            }
            def update_status():    #FAKE OCPP
                socket.set_available()
            timer = Timer(60, update_status)    #TIMER FOR SOCKET RESET
            timer.start() 
            
            return Response(message, status=200)

        #check if the problem is with the socket
        elif( not socket.is_available() and timeDifference<=timedelta(minutes=5)):
            chargeStatus="There are problems with the socket, sorry for the inconvinience"
            return Response(chargeStatus, status=500)

        #the booking is expired if we reach this point
        else:
            chargeStatus="your booking has expired"
            return Response(chargeStatus, status=400)

    #the booking time has not yet arrived
    else:
        chargeStatus="Booking time has not yet arrived"
        return Response(chargeStatus, status=400)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getSocket(request, pk):
    socket = Socket.objects.get(id=pk)
    serializer = SocketSerializer(socket, many=False)
    return Response(serializer.data)

#utils method to hard reset the socket for test purposes
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def resetSocket(request, pk):
    socket = Socket.objects.get(id=pk)
    socket.set_available()
    return Response(status=200)

    
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def startCharge(request):
    #initialize response
    
    chargeStatus="Sorry this socket is not available for charging at the moment"
    #load socket
    socket=Socket.objects.filter(id=request.data['socket']).first()
    print(socket.is_available())
    if(socket.is_available()):
        currentDateTime = datetime.now()
        delta=timedelta(minutes=10)
        bookings=Booking.objects.filter(socket=socket.get_id(), date=currentDateTime.date(), time__range=((currentDateTime-delta).time(), (currentDateTime+delta).time()))
        if(len(bookings)==0):
            message = {
                "socket": request.data['socket'],
                "status": "Charge Started"
            }
            socket.set_charging()
            print(socket.get_availability())
            def update_status():    #FAKE OCPP
                socket.set_available()
            timer = Timer(60, update_status)    #TIMER FOR SOCKET RESET
            timer.start()    
            return Response(message, status=200)
        else:
            print(bookings)
            chargeStatus="Sorry this socket is booked for this time Frame"

    return Response(chargeStatus, status=400)


def update_status(socket):    #FAKE OCPP
                socket.set_available()






#class bookingCheckAPIView(generics.CreateAPIView):
#    serializer_class = CreateChargingStationSerializer
#
#    def post(self, request, *args, **kwargs):
#    
#        serializer = self.get_serializer(data=request.data)
#        serializer.is_valid(raise_exception=True)
#        station = serializer.save()
#        return Response({
#            "station": ChargingStationSerializer(station, context=self.get_serializer_context()).data,
#            "message": "Station Registered Successfully.",
#        })
