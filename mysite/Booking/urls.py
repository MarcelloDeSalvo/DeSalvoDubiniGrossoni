from django.urls import path
from Booking.views import BookingAPIView, RegisterBookingAPIView, getBookingsByUser, RemoveBookingAPIView


urlpatterns = [
  path("api/booking/",BookingAPIView.as_view()),
  path("api/registerbooking/",RegisterBookingAPIView.as_view()),
  path("api/getBookings", getBookingsByUser),
  path("api/removeBooking/",RemoveBookingAPIView.as_view()),
]