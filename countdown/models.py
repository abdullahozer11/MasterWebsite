from django.db import models


class ParisTargetDate(models.Model):
    date = models.DateTimeField()

    def __unicode__(self):
        return self.date
