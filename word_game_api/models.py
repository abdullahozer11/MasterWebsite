from django.db import models


class Word(models.Model):
    date_created = models.DateField(auto_now_add=True)
    letters = models.CharField(max_length=30)

    def __str__(self):
        return f'letters: {self.letters}'
