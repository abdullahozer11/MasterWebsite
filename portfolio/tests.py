"""tests.py. Create your test cases here."""
from django.contrib.staticfiles import finders
from django.test import TestCase


from django.urls import reverse


class PortfolioTest(TestCase):
    """
    TestCase class
    """
    def test_index_url(self):
        """
        view the index page and check response code.
        :return:
        """
        response = self.client.get(reverse('portfolio'))
        self.assertEqual(response.status_code, 200)

    def test_wrong_url_returns_404(self):
        """
        view non-existing page and check 404 response code.
        :return:
        """
        response = self.client.get('/something/really/weird/')
        self.assertEqual(response.status_code, 404)

    def test_404_image(self):
        """
        find the 404 image and assert file found.
        :return:
        """
        result = finders.find('404.svg')
        self.assertNotEqual(result, None)
