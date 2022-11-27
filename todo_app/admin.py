from django.contrib import admin

# Register your models here.
from todo_app.models import ToDoList, ToDoItem

admin.site.register(ToDoList)
admin.site.register(ToDoItem)
