from django.test import TestCase
from restaurant.models import menu

# Create your tests here.
class TestMenu(TestCase):
    def test_get_item(self):
        item = menu.objects.create(item="IcreCream", price=20, inventory=100)
        itemstr = item.get_item()

        self.assertEqual(itemstr, "IcreCream: 20")
