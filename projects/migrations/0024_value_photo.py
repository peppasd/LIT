# Generated by Django 3.0.8 on 2020-07-17 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='value',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='values', to='projects.Photo'),
        ),
    ]