"signals.py signals of portfolio2. Put your signals here."
from django.db.models.signals import post_delete
from django.dispatch import receiver

from portfolio2.models import DemoApp


@receiver(post_delete, sender=DemoApp)
def remove_file_from_s3(sender, instance, using, **kwargs):
    instance.image.delete(save=False)
