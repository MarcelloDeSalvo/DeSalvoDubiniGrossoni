from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from django.http import JsonResponse, HttpResponse
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
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
    # Extract the relevant information from the request
    # Create the booking request payload
    response = requests.get('http://127.0.0.1:8001/OCPI/getChargingStations')
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
    print(newRequest)
    response = requests.post('http://127.0.0.1:8001/OCPI/makebooking/', data=newRequest)    
    if response.status_code == 200:
        # Process the response
        print(response.json()) # print the response
        return "yes"
         # return the response
    else:
        return "no"
