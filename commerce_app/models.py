import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default="Men's Shirt")
    price = models.FloatField(default=0.00)
    photo = models.ImageField(default="default.jpg", upload_to="product_photos")
    color = models.CharField(max_length=20, default="black")
    sizes = [('S', 'SMALL'), ('M', 'MEDIUM'), ('L', 'LARGE'), ('XL', 'X-LARGE')]
    size = models.CharField(default='M', choices=sizes, max_length=10)
    favourites = models.ManyToManyField(User, related_name='favourites', blank=True)
    quantity = models.IntegerField(default=50)

    def __str__(self):
        return self.name

class OrderProduct(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    product = models.ForeignKey(Product, on_delete=CASCADE)
    in_cart_quantity = models.IntegerField(default=1)

class Profile(models.Model):
    name = models.CharField(max_length=30, default="Jean Dupont")
    email = models.EmailField(default="jean.dupont@gmail.com")
    mobile = models.CharField(max_length=15, default="07 69 92 92 92")
    address = models.CharField(max_length=99, default="Saint Cyr L'Ecole, Paris")
    user = models.OneToOneField(User, on_delete=CASCADE)
    photo = models.ImageField(default="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3.webp",
                              upload_to="profile_photos")
    roles = [('C', 'Client'), ('V', 'Vendor')]
    role = models.CharField(default='C', choices=roles, max_length=6)

    def __str__(self):
        return self.user.username
