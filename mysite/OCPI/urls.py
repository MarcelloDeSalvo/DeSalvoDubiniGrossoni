from django.urls import path
from .views import requestChargingStations
urlpatterns = [
  path("OCPI/getChargingStations", requestChargingStations)
]