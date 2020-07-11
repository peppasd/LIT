from django.db import models
from django.contrib.auth.models import User
import datetime
import uuid
from django.dispatch import receiver


# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Project(models.Model):
    name = models.CharField(max_length=160)
    description = models.CharField(max_length=160)
    progress = models.IntegerField(default=0)
    created = models.DateField(default=datetime.date.today)
    members = models.ManyToManyField(Member, blank=True)
    owners = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name

#add  isTagged boolean set it to method call that checks if given photo instance has a tag

class Photo(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='')
    photo = models.FileField(blank=True)
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    def isTagged(self):
        if len(self.tag_set.all())>0:
            return True
        return False




class Label(models.Model):
    name = models.CharField(max_length=160)
    type = models.CharField(max_length=160)
    project = models.ForeignKey(Project, related_name='labels', on_delete=models.CASCADE, null=True, blank=True)

class Value(Label):
    val = models.CharField(max_length=160)
    if type=="Boolean":
        val = models.NullBooleanField()
    elif type=="Integer":
        val = models.IntegerField(default=0)
    elif type=="Float":
        val = models.FloatField(default=0)
    photo = models.ForeignKey(Photo, related_name='values', on_delete=models.CASCADE)
    label = models.ForeignKey(Label, related_name='values', on_delete=models.CASCADE) 






# remove photo from s3 as well
@receiver(models.signals.post_delete, sender=Photo)
def remove_file_from_bucket(sender, instance, using, **kwargs):
    instance.photo.delete(save=False) 
