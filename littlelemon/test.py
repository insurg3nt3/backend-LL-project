from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title = "Icecream", price = 90, inventory=100 )
        itemstr = item.get_item()

        self.assertEqual(itemstr, "Icecream : 90")