"""This is apps.py of todo_app"""
from django.apps import AppConfig


class TodoAppConfig(AppConfig):
    """
    This is TodoAppConfig class to configure todo_app application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo_app'
