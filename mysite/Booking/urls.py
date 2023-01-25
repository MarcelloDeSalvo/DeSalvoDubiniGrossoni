from django.urls import path
from Booking.views import BookingAPIView, RegisterBookingAPIView

urlpatterns = [
  path("api/booking/",BookingAPIView.as_view()),
  path("OCPI/makebooking/",RegisterBookingAPIView.as_view()),
  path("api/registerBooking/",RegisterBookingAPIView.as_view()),
]