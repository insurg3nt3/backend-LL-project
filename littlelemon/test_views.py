from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class MenuItemsViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(username='admin', password='admin')
        self.token = Token.objects.create(user=self.user)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.menu1 = Menu.objects.create(title='Pizza', price=10.99, inventory=100)
        self.menu2 = Menu.objects.create(title='Pasta', price=8.99, inventory=50)

        self.url = reverse('menuitems-list')

    def test_get_menuitems(self):
        self.assertTrue(self.client._credentials['HTTP_AUTHORIZATION'].startswith('Token '))

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.data, serializer.data)

    def test_create_menuitem(self):
        self.assertTrue(self.client._credentials['HTTP_AUTHORIZATION'].startswith('Token '))

        data = {
            'title': 'Salad',
            'price': 5.99,
            'inventory': 30
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Menu.objects.count(), 3)
        salad = Menu.objects.get(title='Salad')
        self.assertAlmostEqual(float(salad.price), data['price'], places=2)