from django.test import TestCase, Client
from django.urls import reverse
from restaurant.models import menu
from restaurant.views import MenuItemView

class TestMenuView(TestCase):

    def setUp(self):
        self.client = Client()
        menu.objects.create(item="IcreCream", price=20, inventory=100)
    def test_getall(self):

        response = self.client.get("/restaurant/menu/")
        print(response.json())
        resp_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(resp_data), 1)