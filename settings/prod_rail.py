"""prod.py. Put your railway app production settings here."""
import sys
import dj_database_url
from .base import *

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", None)
DEBUG = os.getenv("DEBUG", "False") == "True"
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS").split(",")

if len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
    if os.getenv("DATABASE_URL") is None:
        raise Exception("DATABASE_URL environment variable not defined")
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }

MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    BASE_DIR / 'static',
)
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_ROOT = BASE_DIR / "media"

CSRF_TRUSTED_ORIGINS = [
    "https://apojean.com",
    "https://www.apojean.com",
    "https://django-server-production-ee9c.up.railway.app",
]

CORS_ORIGIN_WHITELIST = [
    "https://apojean.com",
    "https://www.apojean.com",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
