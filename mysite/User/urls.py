from django.urls import path
from User.views import RegisterUserAPIView, UserAPIView, isLogged

urlpatterns = [
  path("api/user/",UserAPIView.as_view()),
  path('api/register/',RegisterUserAPIView.as_view()),
  path('api/isLogged/', isLogged, name='isLogged'),
]