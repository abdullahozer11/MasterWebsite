# Generated by Django 4.1.3 on 2023-04-27 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demoapp',
            name='img_url',
        ),
        migrations.AddField(
            model_name='demoapp',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='portfolio2/app_images/'),
        ),
    ]