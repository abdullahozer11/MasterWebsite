from django.test import TestCase
from django.urls import reverse
import json

from word_game_api.views import is_word_in_dictionary


class TestWordValidation(TestCase):
    def test_validate_word_post_valid_word(self):
        url = reverse('words_api:validate')
        data = {'word': 'HELLO'}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'answer': 'valid'})

    def test_validate_word_post_invalid_word(self):
        url = reverse('words_api:validate')
        data = {'word': 'XYZTP'}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'answer': 'invalid'})

    def test_validate_word_get(self):
        url = reverse('words_api:validate')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'answer': 'Only POST requests are allowed'})

    def test_is_word_in_dictionary_valid_word(self):
        result = is_word_in_dictionary('HELLO')
        self.assertEqual(result, True)

    def test_is_word_in_dictionary_invalid_word(self):
        result = is_word_in_dictionary('XYZTP')
        self.assertEqual(result, False)
