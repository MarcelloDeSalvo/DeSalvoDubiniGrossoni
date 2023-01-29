from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes
from ChargingStation.models import ChargingStation
from Socket.models import Socket
from ChargingStation.views import getChargingStations
from ChargingStation.serializers import ChargingStationSerializer
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
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def requestChargingStations(request):
    stations = ChargingStation.objects.all()
    serializer = ChargingStationSerializer(stations, many=True)
    
    if stations==None:
        return Response("there are no stations", status=200)
    print("OCPI sendStations here")
    print (stations)
    #return serializer.data in a response format
    return  Response(serializer.data, status=200)
   


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def startChargeFromBooking(request):

    chargeStatus=""
    date=request.data['date']
    time=request.data['time']
    currentDateTime = datetime.now()
    timeDifference= abs(time - currentDateTime.time())

    if (date==currentDateTime.date() and timeDifference<=timedelta(minutes=5) and socket.is_available()):
        socket=Socket.objects.filter(id=request.data['socket']).first()
        socket.set_unavailable()
        chargeStatus="Charge Started"
        return Response(chargeStatus, status=200)
    elif(not socket.is_available()):
        chargeStatus="There are problems with the socket, sorry for the inconvinience"
        return Response(chargeStatus, status=500)
    else:
        chargeStatus="Charge not started, please try again later"
        return Response(chargeStatus, status=500)










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
