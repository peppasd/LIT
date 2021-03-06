# Generated by Django 3.0.8 on 2020-07-10 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20200710_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160)),
                ('type', models.CharField(max_length=160)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labels', to='projects.Project')),
            ],
        ),
    ]
