from django.contrib import admin

# Register your models here.
from commerce_app.models import Client, Product, Vendor

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Vendor)