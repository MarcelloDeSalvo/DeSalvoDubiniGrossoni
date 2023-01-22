from django.urls import path
from ChargingStation.views import RegisterChargingStationAPIView

urlpatterns = [
  path("api/ChargingStation/",RegisterChargingStationAPIView.as_view()),
]