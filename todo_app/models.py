"""models.py file for todo_app. Create your models here"""
# pylint: disable=no-member
from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from django.utils import timezone


def one_week_hence():
    """
    return one week from now
    :return:
    """
    return timezone.now() + timezone.timedelta(days=7)

class ToDoList(models.Model):
    """
    ToDoList model. This model represents the _todo_list containing tasks.
    """
    user = models.ForeignKey(User, on_delete=CASCADE, default=None)
    title = models.CharField(max_length=100)

    # pylint: disable=too-few-public-methods
    class Meta:
        """set class meta attributes here"""
        unique_together = 'user', 'title'

    def __str__(self):
        return f'{self.title}'

class ToDoItem(models.Model):
    """
    ToDoItem model. This model represents the tasks.
    """
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, default=None)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=CASCADE)

    def __str__(self):
        return f'{self.title}'

    # pylint: disable=too-few-public-methods
    class Meta:
        """set class meta attributes here"""
        ordering = ["due_date"]
