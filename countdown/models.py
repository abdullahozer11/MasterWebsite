from django.db import models


class TargetDate(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
