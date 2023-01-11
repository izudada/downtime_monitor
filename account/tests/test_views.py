from django.test import TestCase, Client
from django.urls import reverse
from account.models import User
import json


class TestViews(TestCase):
    def test_register_view(self):
        client = Client()
        respone = client.post(
                reverse('register'), 
                {
                    "email": "maryann@gmail.com",
                    "first_name": "mary",
                    "last_name": "ann",
                    "username": "marryann",
                    "password": "test12345",
                    "password2": "test12345"
                }
            )
        print(respone)
        self.assertEquals(respone.status_code, 200)
        self.assertEquals(
                respone.data['message'], 
                'user registered successfully'
            )
            