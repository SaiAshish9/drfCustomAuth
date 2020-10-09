from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker
# python manage.py test
from authentication.models import User


class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.fake=Faker()

        self.user_data={
            'email':self.fake.email(),
            'username': self.fake.email().split('@')[0],
            'password':self.fake.email(),
        }

        # import pdb
        # pdb.set_trace()

# type-> self.user_data

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
