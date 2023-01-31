import json
from django.test import Client, TestCase
from User.models import User
from Booking.models import Booking, BookingManager
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your tests here.
# Create some tests for the Booking app

class TestBookings(TestCase):

    # Runs before each test
    def setUp(self):
        user = User.objects.create_user("mail@mail.it", "Giacomo", "Leopardi", "password123")
        bookingManager = BookingManager()
        bookingManager.create_booking(user=user, date="2020-01-01", time="12:00:00", stationID="stationID", socketID="socketID", cpmsID="cpmsID", stationAddress="address")
        # give the client a valid token
        token = self.client.post('/api/token/', {"email": "mail@mail.it", "password": "password123"})
        self.client = Client(HTTP_AUTHORIZATION='Bearer ' + token.data['access'])

    def test_booking_insertion(self):
        booking = BookingManager()
        user = User.objects.get_by_email("mail@mail.it")
        booking = booking.get_bookings_by_user(user)[0]
        self.assertEqual(booking.user, user)
        self.assertEqual(str(booking.date), "2020-01-01")
        self.assertEqual(str(booking.time), "12:00:00")
        self.assertEqual(booking.stationID, "stationID")
        self.assertEqual(booking.socketID, "socketID")
        self.assertEqual(booking.cpmsID, "cpmsID")
        self.assertEqual(booking.stationAddress, "address")

    def test_booking_retrieval(self):
        bookingManager = BookingManager()
        user = User.objects.get_by_email("mail@mail.it")
        booking1 = bookingManager.get_bookings_by_user(user)[0]
        id = booking1.get_id()
        booking2 = bookingManager.get_booking_by_id(id)
        self.assertEqual(booking1.user, booking2.user)
        self.assertEqual(booking1.id, booking2.id)
        self.assertEqual(booking1.date, booking2.date)
        self.assertEqual(booking1.time, booking2.time)
        self.assertEqual(booking1.stationID, booking2.stationID)
        self.assertEqual(booking1.socketID, booking2.socketID)
        self.assertEqual(booking1.cpmsID, booking2.cpmsID)

    def test_booking_deletion(self):
        bookingManager = BookingManager()
        user = User.objects.get_by_email("mail@mail.it")
        booking = bookingManager.get_bookings_by_user(user)[0]
        booking.delete()
        self.assertEqual(len(bookingManager.get_bookings_by_user(user)), 0)

    """ CANNOT TEST THIS BECAUSE OF CPMS REQUIRED CONNECTION
        def test_remove_booking_api_endpoint(self):
        bookingManager = BookingManager()
        user = User.objects.get_by_email("mail@mail.it")
        self.assertEqual(len(bookingManager.get_bookings_by_user(user)), 1)
        id = bookingManager.get_bookings_by_user(user)[0].id
        json_data = json.dumps({'id': id})
        response = self.client.delete('/api/removeBooking/', json_data, content_type='application/json')
        self.assertEqual(response.status_code, 200) """

    def test_get_bookings_api_endpoint(self):
        bookingManager = BookingManager()
        user = User.objects.get_by_email("mail@mail.it")
        self.assertEqual(len(bookingManager.get_bookings_by_user(user)), 1)
        response = self.client.get('/api/getBookings')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['user'], user.id)
