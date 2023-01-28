from django.shortcuts import render
from rest_framework.response import Response
from .serializers import BookingSerializer, CreateBookingSerializer
from rest_framework import generics
from .models import Booking
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
class BookingAPIView(generics.RetrieveAPIView):
    serializer_class = BookingSerializer

    def get_object(self):
        return self.request.user


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class RegisterBookingAPIView(generics.CreateAPIView):
    serializer_class = CreateBookingSerializer

    # Return success message after successful registration
    def post(self, request, *args, **kwargs):
        # Add user to request data object
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        booking = serializer.save()
        return Response({
            "booking": BookingSerializer(booking, context=self.get_serializer_context()).data,
            "message": "Booking Registered Successfully.",
        })


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class RemoveBookingAPIView(generics.DestroyAPIView):

    def delete(self, request):
        
        reservation = Booking.objects.filter(time=request.data['time'], date=request.data['date'], user=request.data['email'], chargingStation=request.data['chargingStation'], socket=request.data['socket']).first()
        reservation.delete()
        return Response({
            "message": "Discount deleted Successfully.",
        })
    
