""" This is admin.py file of Portfolio2 to register models in admin panel"""
from django.contrib import admin

# Register your models here.
from portfolio2.models import CustomerFormModel, DemoApp

admin.site.register(CustomerFormModel)
admin.site.register(DemoApp)
