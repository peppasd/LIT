from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    pwd = models.CharField(max_length=256)

    def __str__(self):
        return self.first_name + " " + self.last_name
