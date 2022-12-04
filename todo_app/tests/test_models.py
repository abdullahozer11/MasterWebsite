"""test_models.py. Create your model tests here."""
# pylint: disable=no-member
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import TestCase

from todo_app.models import ToDoList, ToDoItem


class ToDoListTest(TestCase):
    """
    ToDoListTest
    TestCase class to test basic functionalities for todo_app models.
    """
    user = None

    def setUp(self) -> None:
        """
        Create a new user in setup method.
        :return:
        """
        self.user = User.objects.create_user(username='testuser', password='password')

    def create_todolist(self, title="Only a test list"):
        """
        Create a new todo_list.
        :param title:
        :return:
        """
        return ToDoList.objects.create(user=self.user, title=title)

    def create_todoitem(self):
        """
        Create a new todo_item.
        :return:
        """
        todo_list = ToDoList.objects.create(user=self.user)
        return ToDoItem.objects.create(title="Test item", todo_list=todo_list)

    def test_todolist_creation(self):
        """
        Test todo_list creation.
        :return:
        """
        obj = self.create_todolist()
        self.assertTrue(isinstance(obj, ToDoList))
        self.delete_todolist()

    def test_todoitem_creation(self):
        """
        Test todo_item creation.
        :return:
        """
        obj = self.create_todoitem()
        self.assertTrue(isinstance(obj, ToDoItem))

    def test_todolist_with_same_name(self):
        """
        Test todo_list creation when there is a list with the same name.
        :return:
        """
        self.create_todolist()
        try:
            self.create_todolist()
        except IntegrityError:
            return
        raise IntegrityError("Could create two lists with same name")

    def delete_todolist(self, title="Only a test list"):
        """
        Test deleting todo_list.
        :param title:
        :return:
        """
        obj = ToDoList.objects.get(user=self.user, title=title)
        obj.delete()
