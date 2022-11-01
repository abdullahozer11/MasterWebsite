from django.contrib import admin

# Register your models here.
from commerce_app.models import Product, Profile, OrderProduct, InventoryProduct

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(InventoryProduct)
admin.site.register(OrderProduct)
