# Generated by Django 3.0.8 on 2020-07-10 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20200710_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='labels', to='projects.Project'),
        ),
    ]