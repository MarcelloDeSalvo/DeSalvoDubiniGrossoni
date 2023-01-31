from django.urls import path
from .views import get_chargingStations, start_charging_from_booking, get_ChargingSocket, get_ChargingStationByID, start_charge, stop_charge

urlpatterns = [
  path("OCPI/getChargingStations", get_chargingStations),
  path("OCPI/startChargingFromBooking", start_charging_from_booking),
  path("OCPI/getSocket/<str:pk>/", get_ChargingSocket),
  path("OCPI/getChargingStationById/<str:pk>/", get_ChargingStationByID),
  path("OCPI/startCharge", start_charge),
  path("OCPI/stopCharge/<str:pk>/", stop_charge),
]