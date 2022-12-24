"""local.py. Put your local settings here."""
import sys
import dj_database_url

from .base import *


SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "Not a secret! Do not put the real me in vcs !")
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
DEBUG = True
DEVELOPMENT_MODE = True

if DEVELOPMENT_MODE is True:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
    if os.getenv("DATABASE_URL") is None:
        raise Exception("DATABASE_URL environment variable not defined")
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }

# https://spacepo.ams3.digitaloceanspaces.com/
USE_SPACES = os.getenv("USE_SPACES", "False") == "True"
if USE_SPACES:
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_ENDPOINT_URL = os.getenv("AWS_S3_ENDPOINT_URL")
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # static
    AWS_LOCATION = os.getenv("AWS_LOCATION")
    STATICFILES_STORAGE = 'master_website.storage_backends.StaticStorage'
    AWS_S3_SIGNATURE_VERSION = 's3v4'
    # media
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_ENDPOINT_URL}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'master_website.storage_backends.PublicMediaStorage'
else:
    MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATICFILES_DIRS = (BASE_DIR / 'static',)

STATIC_ROOT = BASE_DIR / "static-cdn"
MEDIA_ROOT = BASE_DIR / "media"
