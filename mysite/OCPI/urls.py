from django.urls import path
from .views import get_chargingStations, start_charging_from_booking, get_ChargingSocket

urlpatterns = [
  path("OCPI/getChargingStations", get_chargingStations),
  path("OCPI/startChargingFromBooking", start_charging_from_booking),
  path("OCPI/getSocket/<str:pk>/", get_ChargingSocket),
]