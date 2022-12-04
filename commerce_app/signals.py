"""signals.py. Create your signals here."""
# pylint: disable=no-member
# pylint: disable=unused-argument
import os

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from .models import User, Profile, Product


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Create a profile each time a new user is created.

    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_delete, sender=Product)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    If a product is deleted, delete its photo from the database.

    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)
