from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=160)
    description = models.CharField(max_length=160)
    progress = models.IntegerField()    
    created = models.DateField()
    labeled_photos = models.IntegerField()
    photos_total = models.IntegerField()
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name