"""This is word game api urls file"""
from django.urls import path

from word_game_api.views import get_word, validate_word

app_name = "words_api"

urlpatterns = [
    path('get/', get_word, name='get'),
    path('validate/', validate_word, name='validate'),
]
