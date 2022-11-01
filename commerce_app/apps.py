from django.apps import AppConfig


class CommerceAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'commerce_app'

    def ready(self):
        import commerce_app.signals