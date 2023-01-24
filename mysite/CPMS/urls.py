from django.urls import path
from .views import RegisterCPMSAPIView, getCPMS

urlpatterns = [
  path("api/registerCPMS/",RegisterCPMSAPIView.as_view()),
  path("api/cpms/",getCPMS),
]