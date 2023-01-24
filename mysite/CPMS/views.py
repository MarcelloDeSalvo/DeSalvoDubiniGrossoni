from django.shortcuts import render
from rest_framework.response import Response

from .models import CPMS, CPMSManager
from .serializers import CPMSSerializer, CreateCPMSSerializer
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
    serializer_class = CPMSSerializer

    def get_object(self):
        return self.request.user


@authentication_classes([])
@permission_classes([])
class RegisterCPMSAPIView(generics.CreateAPIView):
    serializer_class = CreateCPMSSerializer

    def post(self, request, *args, **kwargs):
    
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cpms = serializer.save()
        return Response({
            "station": CPMSSerializer(cpms, context=self.get_serializer_context()).data,
            "message": "Station Registered Successfully.",
        })


# Return all charging stations
# Suitable for the EMSP read only view
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getCPMS(request):
    cpms = CPMS.objects.all()
    serializer = CPMSSerializer(cpms, many=True)
    return Response(serializer.data)

# Return a specific charging station
# Suitable for the EMSP read only view
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getCPMS(request, pk):
    cpms = CPMS.objects.get(id=pk)
    serializer = CPMSSerializer(cpms, many=False)
    return Response(serializer.data)
    