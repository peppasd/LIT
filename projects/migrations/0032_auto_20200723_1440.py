# Generated by Django 3.0.8 on 2020-07-23 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0031_auto_20200722_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='title',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='url',
        ),
    ]