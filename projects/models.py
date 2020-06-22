from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=160)
    description = models.CharField(max_length=160)
    progress = models.IntegerField(default=0)    
    created = models.DateField(default=datetime.date.today)
    labeled_photos = models.IntegerField(default=0)
    photos_total = models.IntegerField(default=0)
    labels=models.CharField(max_length=160, default='')
    user_tmp=models.CharField(max_length=1024, default='')
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name
