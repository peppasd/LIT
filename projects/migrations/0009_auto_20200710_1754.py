# Generated by Django 3.0.8 on 2020-07-10 15:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0008_auto_20200710_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='owners',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
