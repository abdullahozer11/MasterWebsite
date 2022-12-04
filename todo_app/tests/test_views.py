"""test_views.py create your view tests for the commerce_app here"""
from django.contrib.auth.models import User
from django.test import TestCase

from django.urls import reverse


# Create your tests here.
class ToDoViewLoggedInTest(TestCase):
    """
    ToDoViewLoggedInTest
    Test todo_app views with an authenticated user.
    """
    user = None

    def setUp(self):
        """
        Setup method to create and log in user.
        :return:
        """
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.force_login(self.user)

    def test_index_view(self):
        """
        view the page and check response code.
        :return:
        """
        response = self.client.get(reverse('todo:index'))
        self.assertEqual(response.status_code, 200)

    def test_404_view(self):
        """
        view a non-existing page and check 404 response code.
        :return:
        """
        response = self.client.get('todo/something/weird')
        self.assertEqual(response.status_code, 404)

class ToDoViewLoggedOutTest(TestCase):
    """
    ToDoViewLoggedOutTest
    Test todo_app views when without user authentication.
    """

    def test_login_view(self):
        """
        view the page and check response code.
        :return:
        """
        response = self.client.get(reverse('todo:login'))
        self.assertEqual(response.status_code, 200)

    def test_signup_view(self):
        """
        view the page and check response code.
        :return:
        """
        response = self.client.get(reverse('todo:signup'))
        self.assertEqual(response.status_code, 200)
