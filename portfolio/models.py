from django.db import models


# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=20)
    icon = models.ImageField(upload_to='portfolio/skill_icons')

    def __str__(self):
        return self.name
