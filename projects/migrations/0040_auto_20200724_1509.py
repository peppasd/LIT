# Generated by Django 3.0.8 on 2020-07-24 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0039_auto_20200724_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
