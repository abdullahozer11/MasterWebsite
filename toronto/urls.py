"""This is Toronto app urls file"""
from django.urls import path

from toronto.views import TorontoView

app_name = 'toronto'
urlpatterns = [
    path('', TorontoView.as_view(), name='index'),
]
