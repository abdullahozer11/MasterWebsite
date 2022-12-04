"""models.py file for portfolio. Create your models here"""
from django.db import models


# Create your models here.
class Skill(models.Model):
    """
    Skill model. This model represents the software skills that I personally acquired.
    """
    name = models.CharField(max_length=20)
    icon = models.ImageField(upload_to='portfolio/skill_icons')

    def __str__(self):
        return f'{self.name}'
