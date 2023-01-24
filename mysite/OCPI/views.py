from django.shortcuts import render
from rest_framework.response import Response
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



class bookingCheckAPIView(generics.CreateAPIView):
    serializer_class = CreateChargingStationSerializer

    def post(self, request, *args, **kwargs):
    
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        station = serializer.save()
        return Response({
            "station": ChargingStationSerializer(station, context=self.get_serializer_context()).data,
            "message": "Station Registered Successfully.",
        })
