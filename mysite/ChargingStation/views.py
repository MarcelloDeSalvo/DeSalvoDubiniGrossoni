from django.shortcuts import render
from rest_framework.response import Response
from Discount.serializers import DiscountSerializer
from ChargingStation.models import ChargingStation, ChargingStationManager
from Discount.models import Discount
from .serializers import ChargingStationSerializer, CreateChargingStationSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
# Create your views here.
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class ChargingStationAPIView(generics.RetrieveAPIView):
    serializer_class = ChargingStationSerializer

    def get_object(self):
        return self.request.user


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class RegisterChargingStationAPIView(generics.CreateAPIView):
    serializer_class = CreateChargingStationSerializer

    def post(self, request, *args, **kwargs):
    
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        station = serializer.save()
        return Response({
            "station": ChargingStationSerializer(station, context=self.get_serializer_context()).data,
            "message": "Station Registered Successfully.",
        })


# Return all charging stations
# Suitable for the EMSP read only view
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getChargingStations(request):
    stations = ChargingStation.objects.all()
    serializer = ChargingStationSerializer(stations, many=True)
    return Response(serializer.data)

# Return a specific charging station
# Suitable for the EMSP read only view
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getChargingStation(request, pk):
    station = ChargingStation.objects.get(id=pk)
    serializer = ChargingStationSerializer(station, many=False)
    discounts = station.applied_stations.all()
    serializerDiscount = DiscountSerializer(discounts, many=True)
    response={
        'station': serializer.data,
        'discounts': serializerDiscount.data
    }

    return Response(response)
    