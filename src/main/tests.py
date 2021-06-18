from django.test import TestCase

class ViewTestCase(TestCase):

    def test_index_loads_properly(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
