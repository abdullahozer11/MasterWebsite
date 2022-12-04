"""models.py file for commerce_app. Create your models here"""
# pylint: disable=no-member
from django.db.models import CASCADE
from django.db import models
from django.contrib.auth.models import User

from django_resized import ResizedImageField


class Product(models.Model):
    """
    Product model. This model represents the merchandise of the eCommerce website.
    """
    SIZES = (
        ('small', 'Size Small'),
        ('medium', 'Size Medium'),
        ('large', 'Size Large'),
        ('x-LARGE', 'Size X-Large'),
    )
    name = models.CharField(max_length=100, default="Men's Shirt")
    price = models.FloatField(default=0.00)
    photo = models.ImageField(upload_to="commerce_app/product_photos")
    color = models.CharField(max_length=20, default="black")
    size = models.CharField(default='medium', choices=SIZES, max_length=10)
    favorites = models.ManyToManyField(User, related_name='favorites', blank=True)
    quantity = models.IntegerField(default=50)
    GENDERS = (
        ('men', 'menwear'),
        ('women', 'womenwear'),
    )
    gender = models.CharField(default='men', choices=GENDERS, max_length=10)

    def __str__(self):
        return f'{self.name}'

    # pylint: disable=too-few-public-methods
    class Meta:
        """set class meta attributes here"""
        ordering = ['id']


class OrderProduct(models.Model):
    """
    OrderProduct model.
    This model represents the product transformed into an order with information related to a purchase.
    """
    user = models.ForeignKey(User, on_delete=CASCADE)
    product = models.ForeignKey(Product, on_delete=CASCADE)
    in_cart_quantity = models.IntegerField(default=1)

    def get_total(self):
        """this method returns the cart total price of a certain ordered product"""
        return self.product.price * self.in_cart_quantity


class Profile(models.Model):
    """
    Profile model.
    This model represents the profile of each user and their personal informations.
    """
    ROLES = (
        ('client', 'CLIENT ROLE'),
        ('vendor', 'VENDOR ROLE'),
    )
    name = models.CharField(max_length=30, default="Jean Dupont")
    email = models.EmailField(default="jean.dupont@gmail.com")
    mobile = models.CharField(max_length=15, default="07 69 92 92 92")
    address = models.CharField(max_length=99, default="Saint Cyr L'Ecole, Paris")
    user = models.OneToOneField(User, on_delete=CASCADE)
    photo = ResizedImageField(size=[500, 500], default="commerce_app/profile_photos/default.png",
                              upload_to="commerce_app/profile_photos")
    role = models.CharField(default='client', choices=ROLES, max_length=6)

    def __str__(self):
        return self.user.username


class CustomerFormModel(models.Model):
    """
    CustomerFormModel.
    This model represents the information passed in contact us form.
    """
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=99)
    message = models.TextField(max_length=500)
