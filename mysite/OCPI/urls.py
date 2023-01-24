from django.urls import path
from .views import get_chargingStations

urlpatterns = [
  path("OCPI/getChargingStations",get_chargingStations),
]