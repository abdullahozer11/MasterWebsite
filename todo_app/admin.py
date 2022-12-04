""" This is admin.py file of todo_app to register models in admin panel"""
from django.contrib import admin

# Register your models here.
from todo_app.models import ToDoList, ToDoItem

admin.site.register(ToDoList)
admin.site.register(ToDoItem)
