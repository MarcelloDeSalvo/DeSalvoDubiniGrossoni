from django.urls import path
from ChargingStation.views import RegisterChargingStationAPIView

urlpatterns = [
  path("api/registerChargingStation/",RegisterChargingStationAPIView.as_view()),
]