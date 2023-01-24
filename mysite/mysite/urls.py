"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views import debug
from django.urls import include, path
from rest_framework.authtoken import views 

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', debug.default_urlconf),
    path('', include('User.urls')),
    path('', include('Discount.urls')),
    path('', include('Socket.urls')),
    path('', include('Booking.urls')),
    path('', include('ChargingStation.urls')),
    path('', include('EnergyProvider.urls')),
    path('polls/', include('polls.urls')),
    path('api-token-auth', views.obtain_auth_token),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
