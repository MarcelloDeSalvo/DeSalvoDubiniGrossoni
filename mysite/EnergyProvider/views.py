from django.shortcuts import render
from rest_framework.response import Response

from Discount.models import Discount
from .serializers import DSO_Serializer, RegisterDSOSerializer, BSS_Serializer, RegisterBSSSerializer
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

@authentication_classes([])
@permission_classes([])
class RegisterBSS(generics.CreateAPIView):
    serializer_class = RegisterBSSSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        bss = serializer.save()
        return Response({
            "bss": RegisterBSSSerializer(bss, context=self.get_serializer_context()).data,
            "message": "BSS Registered Successfully.",
        })