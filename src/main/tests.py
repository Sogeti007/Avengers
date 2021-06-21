from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class ViewMainTestCase(TestCase):
    
    def test_index_loads_properly(self):
        url = reverse("main-home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
