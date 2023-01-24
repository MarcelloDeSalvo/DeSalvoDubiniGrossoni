from django.urls import path
from EnergyProvider.views import RegisterDSO, RegisterBSS

urlpatterns = [
  path("api/registerDSO/",RegisterDSO.as_view()),
  path("api/registerBSS/",RegisterBSS.as_view()),
]