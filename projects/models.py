from django.db import models
from django.contrib.auth.models import User
import uuid
from django.dispatch import receiver

# Create your models here.
class Member(models.Model):
    user = models.ManyToManyField(User, blank=True)

class Project(models.Model):
    name = models.CharField(max_length=160)
    ownerName = models.CharField(max_length=160, default="")
    description = models.CharField(max_length=160)
    progress = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(Member, blank=True)
    owners = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Photo(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created = models.DateTimeField(auto_now_add=True)
    file = models.FileField()
    name = models.CharField(max_length=512)
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE, null=True, blank=True)    
    
    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete( *args, **kwargs)


class Label(models.Model):
    name = models.CharField(max_length=160)
    type = models.CharField(max_length=160)
    project = models.ForeignKey(Project, related_name='labels', on_delete=models.CASCADE, null=True, blank=True)

class Value(models.Model):
    label = models.ManyToManyField(Label, related_name='values', blank=True)
    val = models.CharField(max_length=160)    
    photo = models.ForeignKey(Photo, related_name='values', on_delete=models.CASCADE, null=True, blank=True)

# remove photo from cloud storage as well

@receiver(models.signals.post_delete, sender=Photo)
def remove_file_from_bucket(sender, instance, using, **kwargs):
    instance.file.delete(save=False)
