# Generated by Django 4.1.3 on 2022-11-26 22:09

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('commerce_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=django_resized.forms.ResizedImageField(crop=None, default='commerce_app/profile_photos/default.png', force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[500, 500], upload_to='profile_photos'),
        ),
    ]
