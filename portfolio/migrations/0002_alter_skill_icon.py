# Generated by Django 4.1.3 on 2022-11-26 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='icon',
            field=models.ImageField(upload_to='portfolio/skill_icons'),
        ),
    ]
