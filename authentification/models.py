from django.db import models


# Create your models here.
class User(models.Model):
    # Fields
    first_name = models.CharField(max_length=20, help_text='Please enter your firstname.')
    last_name = models.CharField(max_length=30, help_text='Please enter your lastname.')
    email = models.CharField(max_length=50, help_text='Please enter your email address.')
    pwd = models.EmailField(max_length=256, help_text='Please enter your password.')

    #Metadata
    class Meta:
        ordering = ['-last_name']

    # #Methods
    def __str__(self):
        return self.first_name + " " + self.last_name
