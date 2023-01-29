from django.shortcuts import render
from rest_framework.response import Response

from EnergyProvider.models import DSO, BSS
from ChargingStation.models import ChargingStation
from .serializers import DSO_Serializer, RegisterDSOSerializer, BSS_Serializer, RegisterBSSSerializer, ToggleBSSSerializer, SwitchDSOSerializer
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
class RegisterDSO(generics.CreateAPIView):
    serializer_class = RegisterDSOSerializer

    # Return success message after successful discount add
    def post(self, request, *args, **kwargs):
    
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        dso = serializer.save()
        return Response({
            "dso": RegisterDSOSerializer(dso, context=self.get_serializer_context()).data,
            "message": "DSO Registered Successfully.",
        })

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class RegisterBSS(generics.CreateAPIView):
    serializer_class = RegisterBSSSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        bss = serializer.save()
        bss.get_station().update_prices()
        return Response({
            "bss": RegisterBSSSerializer(bss, context=self.get_serializer_context()).data,
            "message": "BSS Registered Successfully.",
        })

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class ToggleBSS(generics.UpdateAPIView):
    queryset = BSS.objects.all()
    serializer_class = ToggleBSSSerializer

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class SwitchDSO(generics.UpdateAPIView):
    queryset = ChargingStation.objects.all()
    serializer_class = SwitchDSOSerializer
