from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import TestCase

# models test
from todo_app.models import ToDoList, ToDoItem


class ToDoListTest(TestCase):

    user = None

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='testuser', password='password')

    def create_todolist(self, title="Only a test list"):
        return ToDoList.objects.create(user=self.user, title=title)

    def test_todolist_creation(self):
        obj = self.create_todolist()
        self.assertTrue(isinstance(obj, ToDoList))
        self.assertEqual(obj.__str__(), obj.title)
        self.delete_todolist()

    def create_todoitem(self):
        todo_list = ToDoList.objects.create(user=self.user)
        return ToDoItem.objects.create(title="Test item", todo_list=todo_list)

    def test_todoitem_creation(self):
        obj = self.create_todoitem()
        self.assertTrue(isinstance(obj, ToDoItem))
        self.assertEqual(obj.__str__(), obj.title)

    def test_todolist_with_same_name(self):
        self.create_todolist()
        try:
            self.create_todolist()
        except IntegrityError:
            return
        raise IntegrityError("Could create two lists with same name")

    def delete_todolist(self, title="Only a test list"):
        obj = ToDoList.objects.get(user=self.user, title=title)
        obj.delete()
