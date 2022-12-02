from django.contrib.staticfiles import finders
from django.test import TestCase


from django.urls import reverse


class PortfolioTest(TestCase):

    def test_index_url(self):
        response = self.client.get(reverse('portfolio'))
        self.assertEqual(response.status_code, 200)

    def test_wrong_url_returns_404(self):
        response = self.client.get('/something/really/weird/')
        self.assertEqual(response.status_code, 404)

    def test_404_image(self):
        result = finders.find('404.svg')
        self.assertNotEqual(result, None)
