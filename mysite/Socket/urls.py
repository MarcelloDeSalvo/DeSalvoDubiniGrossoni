from django.urls import path
from Socket.views import RegisterSocketAPIView

urlpatterns = [
  path("api/registersocket/",RegisterSocketAPIView.as_view()),
]