from django.apps import AppConfig


class Portfolio2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio2'

    def ready(self):
        import portfolio2.signals
