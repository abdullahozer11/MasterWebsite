"""models.py of portfolio2"""
from django.db import models

from django_resized import ResizedImageField


class CustomerFormModel(models.Model):
    """
    CustomerFormModel.
    This model represents the information passed in contact us form.
    """
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=99)
    message = models.TextField(max_length=500)


class DemoApp(models.Model):
    """
    App.
    This model represents the app we are showcasing in the portfolio.
    """
    title = models.CharField(max_length=30)
    desc = models.TextField(max_length=500)
    url = models.CharField(max_length=200)
    image = ResizedImageField(upload_to='portfolio2/app_images/', size=[500, 700], crop=['middle', 'center'],
                              force_format="WEBP", quality=100, scale=1)

    def __str__(self):
        return self.title
