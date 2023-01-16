from django.urls import path
from .views import RegisterUserAPIView, LoginView, ProfileView, isLogged

urlpatterns = [
  path("get-details/",ProfileView.as_view()),
  path('register/',RegisterUserAPIView.as_view()),
  path('login/', LoginView.as_view()),
  path('isLogged/', isLogged, name='isLogged'),
]