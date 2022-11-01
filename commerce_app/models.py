from django.db import models

# Create your models here.
from django.db.models import CASCADE

class Person(models.Model):
    username = models.CharField(max_length=100, unique=True)
    bio = models.TextField(max_length=999, blank=True, null=True)
    avatar = models.ImageField(default="default.jpg", upload_to="media/product_photos")

class Vendor(Person):
    pass

class Client(Person):
    pass

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=999, blank=True, null=True)
    price = models.IntegerField(default=0)
    photo = models.ImageField(default="default.jpg", upload_to="media/product_photos")
    vendor = models.ForeignKey(Vendor, on_delete=CASCADE)
