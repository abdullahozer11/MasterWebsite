from django.contrib import admin

# Register your models here.
from commerce_app.models import Product, Profile, OrderProduct, CustomerFormModel

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(OrderProduct)
admin.site.register(CustomerFormModel)
