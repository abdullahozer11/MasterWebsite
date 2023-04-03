"""This is count down app urls file"""

from django.urls import path

from countdown.views import ParisView

app_name = 'countdown'
urlpatterns = [
    path('', ParisView.as_view(), name='index')
]
