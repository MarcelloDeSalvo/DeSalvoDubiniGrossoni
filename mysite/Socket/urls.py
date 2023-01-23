from django.urls import path
from Socket.views import RegisterSocketAPIView

urlpatterns = [
  path("api/registerSocket/",RegisterSocketAPIView.as_view()),
]