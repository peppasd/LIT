# Generated by Django 3.0.8 on 2020-07-11 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_remove_project_labeled_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]