# Generated by Django 3.0.8 on 2020-07-17 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0025_auto_20200717_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='value',
            name='label',
        ),
        migrations.AddField(
            model_name='value',
            name='label',
            field=models.ManyToManyField(blank=True, null=True, related_name='values', to='projects.Label'),
        ),
    ]
