from django.shortcuts import render
from rest_framework.response import Response
from .serializers import BookingSerializer, CreateBookingSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes
from rest_framework.permissions import IsAuthenticated
from OCPI.views import validate_booking, validate_delete
from .models import Booking
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
           #set user to email for cpms backend identification key


        request.data['cpmsID'] = 1 #hard set to avoid clash with checks, will be removed later if other cpmss are added
        request.data['user'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        #use OCPI interface to send data to cpms, if validated completes booking registration, if not aborts.
        if(validate_booking(request, request.user.get_email()) == "yes"):   #sends data to OCPI interface to register booking cpms-side
            booking = serializer.save()
            return Response({
                "booking": BookingSerializer(booking, context=self.get_serializer_context()).data,
                "message": "Booking Registered Successfully.",
            })
        else:
            return Response({
                "message": "Booking Failed.",
            })
        
      
# Return bookings by user
#problem, stations are stored as an ID, not with address.
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getBookingsByUser(request):
    User = request.user
    reservations = Booking.objects.filter(user=User)

    print (reservations)
    serializer = BookingSerializer(reservations, many=True)
    return Response(serializer.data)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class RemoveBookingAPIView(generics.DestroyAPIView):

    def delete(self, request):
        id = request.data['id']

        reservation = Booking.objects.filter(id=id).first()
        #extract user, station, socket, time, date from reservation
        #send to OCPI interface to delete booking on cpms side
        print (reservation)
        serverAnswer = validate_delete(reservation.get_user().get_email(), reservation.get_stationID(), reservation.get_socketID(), reservation.get_time(), reservation.get_date())
        if(serverAnswer == "yes"):
            reservation.delete()
            return Response({
                "message": "Discount deleted Successfully.",
            })
        else:
            return Response({
                "message": "Discount deletion failed.",
            })