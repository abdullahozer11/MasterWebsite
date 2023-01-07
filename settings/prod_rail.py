"""prod.py. Put your railway app production settings here."""

from .base import *


SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", None)
DEBUG = os.getenv("DEBUG", "False") == "True"
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS").split(",")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (BASE_DIR / 'static',)
STATIC_ROOT = BASE_DIR / "static-cdn"
MEDIA_ROOT = BASE_DIR / "media"
