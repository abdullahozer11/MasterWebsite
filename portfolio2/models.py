from django.conf.global_settings import MEDIA_URL
from django.db import models

from portfolio2.helpers import ResizedImageField


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
    img = ResizedImageField(upload_to='portfolio2/app_images', default='portfolio2/app_images/default.webp',
                            width=500, height=900)
    url = models.CharField(max_length=200)

    def img_url(self):
        file_ext = str(self.img).split('/')[-1]
        return f"media/portfolio2/app_images/{file_ext}"

    def __str__(self):
        return self.title
