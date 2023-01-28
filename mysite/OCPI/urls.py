from django.urls import path
from .views import requestChargingStations, startChargeFromBooking
urlpatterns = [
  path("OCPI/getChargingStations", requestChargingStations),
  path("OCPI/startChargeFromBooking", startChargeFromBooking)
]