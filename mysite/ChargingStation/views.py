from django.shortcuts import render
from rest_framework.response import Response

from mysite.ChargingStation.models import ChargingStation
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
@authentication_classes([])
@permission_classes([])
class ChargingStationAPIView(generics.RetrieveAPIView):
    serializer_class = ChargingStationSerializer

    def get_object(self):
        return self.request.user


@authentication_classes([])
@permission_classes([])
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
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getChargingStations(request):
    stations = ChargingStation.objects.all()
    serializer = ChargingStationSerializer(stations, many=True)
    return Response(serializer.data)
    