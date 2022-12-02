from django.contrib.auth.models import User
from django.test import TestCase

from django.urls import reverse


# Create your tests here.
class eCommerceViewLoggedInTests(TestCase):

    user = None

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.force_login(self.user)

    def test_index_view(self):
        response = self.client.get(reverse('commerce:index'))
        self.assertEqual(response.status_code, 200)

    def test_404_view(self):
        response = self.client.get('commerce/something/weird')
        self.assertEqual(response.status_code, 404)

    def test_profile_view(self):
        response = self.client.get(reverse('commerce:profile'))
        self.assertEqual(response.status_code, 200)

    def test_testimonial_view(self):
        response = self.client.get(reverse('commerce:testimonial'))
        self.assertEqual(response.status_code, 200)

    def test_about_view(self):
        response = self.client.get(reverse('commerce:about'))
        self.assertEqual(response.status_code, 200)

    def test_products_view(self):
        response = self.client.get(reverse('commerce:product'))
        self.assertEqual(response.status_code, 200)

    def test_contact_view(self):
        response = self.client.get(reverse('commerce:contact'))
        self.assertEqual(response.status_code, 200)

    def test_disclaimer_view(self):
        response = self.client.get(reverse('commerce:disclaimer'))
        self.assertEqual(response.status_code, 200)

    def test_cart_view(self):
        response = self.client.get(reverse('commerce:cart'))
        self.assertEqual(response.status_code, 200)

class eCommerceViewLoggedOutTests(TestCase):

    def test_login_view(self):
        response = self.client.get(reverse('commerce:login'))
        self.assertEqual(response.status_code, 200)

    def test_signup_view(self):
        response = self.client.get(reverse('commerce:signup'))
        self.assertEqual(response.status_code, 200)
