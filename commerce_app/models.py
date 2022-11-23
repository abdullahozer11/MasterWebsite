import os.path

from PIL import Image
from django.contrib.auth.models import User
from django.core.files.storage import default_storage as storage
from django.db import models

# Create your models here.
from django.db.models import CASCADE


THUMBNAIL_SIZE = (400, 400)

class Product(models.Model):
    SIZES = (
        ('small', 'Size Small'),
        ('medium', 'Size Medium'),
        ('large', 'Size Large'),
        ('x-LARGE', 'Size X-Large'),
    )
    name = models.CharField(max_length=100, default="Men's Shirt")
    price = models.FloatField(default=0.00)
    photo = models.ImageField(upload_to="product_photos")
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
        return self.name

    class Meta:
        ordering = ['id']


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
    photo = models.ImageField(default="commerce_app/profile_photos/default.png", upload_to="profile_photos")
    role = models.CharField(default='client', choices=ROLES, max_length=6)

    def __str__(self):
        return self.user.username

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        # generate thumbnail version
        self.generate_thumbnail()
        # delete the original photo
        self.photo.delete(save=False)

    def generate_thumbnail(self):
        file_path = self.photo.name
        file_base_name, file_extension = os.path.splitext(file_path)
        thumbnail_file_path = f"{file_base_name}_thumbnail.jpg"
        f = storage.open(file_path, "rb")
        image = Image.open(f)
        image = image.convert('RGB')
        width, height = image.size

        if width > height:
            delta = width - height
            left = int(delta / 2)
            upper = 0
            right = height + left
            lower = height
        else:
            delta = height - width
            left = 0
            upper = int(delta / 2)
            right = width
            lower = width + upper

        image = image.crop((left, upper, right, lower))
        image = image.resize(THUMBNAIL_SIZE, Image.ANTIALIAS)
        f_mob = storage.open(thumbnail_file_path, "w")
        image.save(f_mob, "JPEG")
        f_mob.close()

    def get_thumbnail_photo_url(self):
        file_path = self.photo.name
        file_base_name, file_extension = os.path.splitext(file_path)
        thumbnail_file_path = f"{file_base_name}_thumbnail.jpg"
        if storage.exists(thumbnail_file_path):
            return storage.url(thumbnail_file_path)
        return None

class CustomerFormModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=99)
    message = models.TextField(max_length=500)
