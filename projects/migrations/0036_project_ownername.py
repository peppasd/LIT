# Generated by Django 3.0.8 on 2020-07-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0035_auto_20200723_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ownerName',
            field=models.CharField(default='', max_length=160),
        ),
    ]
