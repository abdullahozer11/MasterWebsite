"""This is count down app urls file"""
from django.urls import path
from django.views.generic import TemplateView

app_name = 'countdown'
urlpatterns = [
    path('', TemplateView.as_view(template_name='countdown/index.html'), name='index'),
]
