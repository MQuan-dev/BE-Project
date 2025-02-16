from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="Pizza", price=12.99, inventory=50)
        Menu.objects.create(title="Burger", price=9.99, inventory=30)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')  # Đường dẫn API của bạn
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = list(Menu.objects.values("id", "title", "price", "inventory"))
        for item in expected_data:
            item["price"] = str(item["price"])
        self.assertEqual(response.json(), expected_data)
