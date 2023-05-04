from django.db import models

timezone_choices = [
    ('GMT-12', 'GMT-12'), ('GMT-11', 'GMT-11'), ('GMT-10', 'GMT-10'),
    ('GMT-9', 'GMT-9'), ('GMT-8', 'GMT-8'), ('GMT-7', 'GMT-7'),
    ('GMT-6', 'GMT-6'), ('GMT-5', 'GMT-5'), ('GMT-4', 'GMT-4'),
    ('GMT-3', 'GMT-3'), ('GMT-2', 'GMT-2'), ('GMT-1', 'GMT-1'),
    ('GMT', 'GMT'),
    ('GMT+1', 'GMT+1'), ('GMT+2', 'GMT+2'), ('GMT+3', 'GMT+3'),
    ('GMT+4', 'GMT+4'), ('GMT+5', 'GMT+5'), ('GMT+6', 'GMT+6'),
    ('GMT+7', 'GMT+7'), ('GMT+8', 'GMT+8'), ('GMT+9', 'GMT+9'),
    ('GMT+10', 'GMT+10'), ('GMT+11', 'GMT+11'), ('GMT+12', 'GMT+12'),
    ('GMT+13', 'GMT+13'), ('GMT+14', 'GMT+14')
]


class TargetDate(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    timezone = models.CharField(max_length=6, choices=timezone_choices, default='GMT+2')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
