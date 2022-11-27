from django.forms import ModelForm

from todo_app.models import ToDoList, ToDoItem


class ListForm(ModelForm):
    class Meta:
        model = ToDoList
        fields = ['title']

class ItemForm(ModelForm):
    class Meta:
        model = ToDoItem
        exclude = ['todo_list']
