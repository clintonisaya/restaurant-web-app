from django.test import TestCase
from .models import Menu

# Create your tests here.

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", price=80, Inventory=100)
        self.assertEqual(item, "IceCream : 80")