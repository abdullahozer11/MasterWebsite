""" This is admin.py file of portfolio to register models in admin panel"""
from django.contrib import admin

# Register your models here.
from portfolio.models import Skill

admin.site.register(Skill)
