# Generated by Django 4.1.3 on 2023-05-04 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countdown', '0002_targetdate_delete_paristargetdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='targetdate',
            name='timezone',
            field=models.CharField(choices=[('GMT-12', 'GMT-12'), ('GMT-11', 'GMT-11'), ('GMT-10', 'GMT-10'), ('GMT-9', 'GMT-9'), ('GMT-8', 'GMT-8'), ('GMT-7', 'GMT-7'), ('GMT-6', 'GMT-6'), ('GMT-5', 'GMT-5'), ('GMT-4', 'GMT-4'), ('GMT-3', 'GMT-3'), ('GMT-2', 'GMT-2'), ('GMT-1', 'GMT-1'), ('GMT', 'GMT'), ('GMT+1', 'GMT+1'), ('GMT+2', 'GMT+2'), ('GMT+3', 'GMT+3'), ('GMT+4', 'GMT+4'), ('GMT+5', 'GMT+5'), ('GMT+6', 'GMT+6'), ('GMT+7', 'GMT+7'), ('GMT+8', 'GMT+8'), ('GMT+9', 'GMT+9'), ('GMT+10', 'GMT+10'), ('GMT+11', 'GMT+11'), ('GMT+12', 'GMT+12'), ('GMT+13', 'GMT+13'), ('GMT+14', 'GMT+14')], default='GMT+2', max_length=6),
        ),
    ]
