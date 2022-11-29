from unittest import TestCase

from django.contrib.auth.models import User


class CommerceTest(TestCase):
    user = None

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='testuser', password='password')

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_something_that_will_pass(self):
        self.assertFalse(False)

    def test_something_that_will_fail(self):
        self.assertTrue(False)
