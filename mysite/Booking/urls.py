from django.urls import path
from Booking.views import BookingAPIView, RegisterBookingAPIView

urlpatterns = [
  path("api/booking/",BookingAPIView.as_view()),
  path("api/registerbooking/",RegisterBookingAPIView.as_view()),
]