"""This is forms.py of todo_app. Create your model forms here."""
# pylint: disable=too-few-public-methods
from django.forms import ModelForm

from todo_app.models import ToDoList, ToDoItem


class ListForm(ModelForm):
    """
    This form is to create and update _todo_lists.
    """
    class Meta:
        """set class meta attributes here"""
        model = ToDoList
        fields = ['title']

class ItemForm(ModelForm):
    """
    This form is to create and update _todo_items.
    """
    class Meta:
        """set class meta attributes here"""
        model = ToDoItem
        exclude = ['todo_list']
