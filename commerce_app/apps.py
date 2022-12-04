"""This is apps.py of commerce_app"""
#pylint: disable=import-outside-toplevel
#pylint: disable=unused-import

from django.apps import AppConfig


class CommerceAppConfig(AppConfig):
    """
    This is CommerceAppConfig class to configure commerce_app application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'commerce_app'

    def ready(self):
        import commerce_app.signals
