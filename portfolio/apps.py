"""This is apps.py of portfolio"""
from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    """
    This is PortfolioConfig class to configure portfolio application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
