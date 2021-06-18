from django.test import TestCase
from django.urls import reverse
from django.test.client import RequestFactory
from unittest import mock

class ViewRegisterTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_register_without_anything(self):
        url = reverse("register")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_good_register(self):
        url = reverse("register")
        data = {'username': ['Peter'], 'email':['peter@fake.com'], 'first_name':['Peter'], 'last_name':['Müller'], 'password1':['testing123456'], 'password2':['testing123456']}
        
        resp = self.client.get(url)
        data['csrfmiddlewaretoken'] = resp.cookies['csrftoken'].value
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_bad_register(self):
        url = reverse("register")
        data = {'username': ['Peter'], 'email':['peter@fake.com'], 'first_name':['Peter'], 'last_name':['Müller'], 'password1':['1'], 'password2':['2']}
        
        resp = self.client.get(url)
        data['csrfmiddlewaretoken'] = resp.cookies['csrftoken'].value
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)        
        

