import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import CASCADE, Choices


class Product(models.Model):
    SIZES = (
        ('small', 'Size Small'),
        ('medium', 'Size Medium'),
        ('large', 'Size Large'),
        ('x-LARGE', 'Size X-Large'),
    )
    name = models.CharField(max_length=100, default="Men's Shirt")
    price = models.FloatField(default=0.00)
    photo = models.ImageField(default="product_photos/default.png", upload_to="product_photos")
    color = models.CharField(max_length=20, default="black")
    size = models.CharField(default='medium', choices=SIZES, max_length=10)
    favorites = models.ManyToManyField(User, related_name='favorites', blank=True)
    quantity = models.IntegerField(default=50)

    def __str__(self):
        return self.name


class OrderProduct(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    product = models.ForeignKey(Product, on_delete=CASCADE)
    in_cart_quantity = models.IntegerField(default=1)

    def get_total(self):
        return self.product.price * self.in_cart_quantity


class Profile(models.Model):
    ROLES = (
        ('client', 'CLIENT ROLE'),
        ('vendor', 'VENDOR ROLE'),
    )
    name = models.CharField(max_length=30, default="Jean Dupont")
    email = models.EmailField(default="jean.dupont@gmail.com")
    mobile = models.CharField(max_length=15, default="07 69 92 92 92")
    address = models.CharField(max_length=99, default="Saint Cyr L'Ecole, Paris")
    user = models.OneToOneField(User, on_delete=CASCADE)
    photo = models.ImageField(default="profile_photos/default.png", upload_to="profile_photos")
    role = models.CharField(default='client', choices=ROLES, max_length=6)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        pass


class CustomerFormModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=99)
    message = models.TextField(max_length=500)
