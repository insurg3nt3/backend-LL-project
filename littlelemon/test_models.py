from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title = "Icecream", price = 90, inventory=100 )
        itemstr = item.get_item()

        self.assertEqual(itemstr, "Icecream : 90")


class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name = "Alfredo", no_of_guests = 2, booking_date="2024-05-24" )
        itemstr = item.get_item()

        self.assertEqual(itemstr, "Alfredo : 2 : 2024-05-24")