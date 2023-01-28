from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
import os
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from Booking.models import Booking
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
# Create your views here.

#receive request from frontend to get charging stations from external backend via request
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_chargingStations(request):
    cpms_url = os.environ.get('CPMS_URL')
    # Extract the relevant information from the request
    # Create the booking request payload
    
    response = requests.get(cpms_url + 'OCPI/getChargingStations')
    #print json content of the response
    if response.status_code == 200:
        # Process the response
        content = response.content
        return HttpResponse(content)
         # return the response
    else:
        return HttpResponse("failed to fetch charging stations", status=500)


# sends booking data to cpms, return yes if booking is registerd, no otherwise.
def validate_booking(request, mail):
    newRequest={
        "user": mail,
        "chargingStation": request.data['stationID'],
        "socket": request.data['socketID'],
        "time": request.data['time'],
        "date": request.data['date']
    }
    cpms_url = os.environ.get('CPMS_URL')
    response = requests.post(cpms_url +'OCPI/makebooking/', data=newRequest)    
    if response.status_code == 200:
        # Process the response
        return "yes"
         # return the response
    else:
        return "no"


# delete booking from cpms, return yes if booking is deleted, no otherwise.
def validate_delete(mail, stationId, socketId, time, date):
    newRequest={
        "email": mail,
        "chargingStation": stationId,
        "socket": socketId,
        "time": time,
        "date": date
    }
    cpms_url = os.environ.get('CPMS_URL')
    response = requests.delete(cpms_url + 'OCPI/deleteBooking/', data=newRequest)
    if response.status_code == 200:
        # Process the response
        return "yes"
         # return the response
    else:
        return "no"

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def start_charging_from_booking(request):
    print(request.body)
    reservation=Booking.objects.get(id=request.data['id'])

    newRequest={
        "email": reservation.get_user().get_email(),
        "chargingStation": reservation.get_stationID(),
        "socket": reservation.get_socketID(),
        "time": reservation.get_time(),
        "date": reservation.get_date()
    }
    cpms_url = os.environ.get('CPMS_URL')
    response = requests.post(cpms_url + 'OCPI/startChargeFromBooking', data=newRequest)
    if response.status_code == 200:
        # Process the response
        return HttpResponse("started charging", status=200)
         # return the response
    else:
        return HttpResponse(response.content, status=500)
