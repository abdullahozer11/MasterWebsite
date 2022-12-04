"""storage_backends.py. Create custom storage classes to manage static and media file servings."""
# pylint: disable=abstract-method
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    StaticStorage class to overwrite S3Boto3Storage with custom attributes for static file servings.
    """
    location = 'static'
    default_acl = 'public-read'


class PublicMediaStorage(S3Boto3Storage):
    """
    PublicMediaStorage class to overwrite S3Boto3Storage with custom attributes for media servings.
    """
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False
