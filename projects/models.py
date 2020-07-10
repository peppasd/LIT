from django.db import models
from django.contrib.auth.models import User
import datetime
import uuid
from django.dispatch import receiver


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=160)
    description = models.CharField(max_length=160)
    progress = models.IntegerField(default=0)
    created = models.DateField(default=datetime.date.today)
    labeled_photos = models.IntegerField(default=0)
    photos_total = models.IntegerField(default=0)
    labels = models.CharField(max_length=160, default='', blank=True)
    user_tmp = models.CharField(max_length=1024, default='', blank=True)
    users = models.ManyToManyField(User)
    ownerusers = models.ManyToManyField(User)

    def __str__(self):
        return self.name

#add  isTagged boolean set it to method call that checks if given photo instance has a tag

class Tag(models.Model):
    InputTagName = models.CharField(max_length=160)
    inputState = models.CharField(max_length=160)
    project = models.ForeignKey(Project, related_name='tags', on_delete=models.CASCADE)

class Photo(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    photo = models.FileField()
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    def isTagged(self):
        if len(self.tag_set.all())>0:
            return True
        return False



# remove photo from s3 as well
@receiver(models.signals.post_delete, sender=Photo)
def remove_file_from_bucket(sender, instance, using, **kwargs):
    instance.photo.delete(save=False)
