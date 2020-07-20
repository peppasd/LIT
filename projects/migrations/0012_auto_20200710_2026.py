# Generated by Django 3.0.8 on 2020-07-10 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
        migrations.AlterField(
            model_name='label',
            name='type',
            field=models.CharField(choices=[('TEXT', 'Text'), ('BOOLEAN', 'Boolean'), ('INTEGER', 'Integer'), ('FLOAT', 'Float')], default='Text', max_length=160),
        ),
    ]
