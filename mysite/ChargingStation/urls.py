from django.urls import path
from ChargingStation.views import RegisterChargingStationAPIView, getChargingStations, getChargingStation

urlpatterns = [
  path("api/registerChargingStation/",RegisterChargingStationAPIView.as_view()),
  path("api/getChargingStations/",getChargingStations),
  path("api/getChargingStation/<str:pk>/",getChargingStation),

]