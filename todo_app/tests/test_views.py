from django.contrib.auth.models import User
from django.test import TestCase

from django.urls import reverse


# Create your tests here.
class ToDoViewLoggedInTest(TestCase):

    user = None

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.force_login(self.user)

    def test_index_view(self):
        response = self.client.get(reverse('todo:index'))
        self.assertEqual(response.status_code, 200)

    def test_404_view(self):
        response = self.client.get('todo/something/weird')
        self.assertEqual(response.status_code, 404)

class ToDoViewLoggedOutTest(TestCase):

    def test_login_view(self):
        response = self.client.get(reverse('todo:login'))
        self.assertEqual(response.status_code, 200)

    def test_signup_view(self):
        response = self.client.get(reverse('todo:signup'))
        self.assertEqual(response.status_code, 200)
