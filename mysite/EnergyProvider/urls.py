from django.urls import path
from EnergyProvider.views import RegisterDSO, RegisterBSS, ToggleBSS, SwitchDSO, SelectBestProviderAuto

urlpatterns = [
  path("api/registerDSO/",RegisterDSO.as_view()),
  path("api/registerBSS/",RegisterBSS.as_view()),
  path('api/toggleBSS/<int:pk>/', ToggleBSS.as_view()),
  path('api/switchDSO/<int:pk>/', SwitchDSO.as_view()),
  path('api/selectBestProviderAuto/<int:pk>/', SelectBestProviderAuto.as_view()),
]