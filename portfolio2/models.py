from django.db import models


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
    img = models.ImageField(upload_to='portfolio2/app_images')
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title
