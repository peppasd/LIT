from django.contrib.auth.models import User
from .models import Project, Label, Photo


def existsUser(username):
    if User.objects.filter(username=username).exists():
        return True

    return False

def getUser(username):
    return User.objects.get(username=username)

def allUsers_project(project):
    ret = []
    users = project.owners.all()
    for user in users:
        ret.append(user)
    members = project.members.all()
    for member in members:
        ret.append(member.user.first())
    return ret


def allTags_project(project):
    ret = []
    tags = project.labels.all()
    for tag in tags:
        ret.append(tag)
    return ret

def calProgress(project):
    imgs = list(project.images.all())
    count_images = len(imgs)
    count_getag = 0
    for img in imgs:
        val = list(img.values.all())
        if len(val) != 0:
            count_getag += 1
    if count_images == 0:
        return 0,0,0
    return int((count_getag / count_images) * 100), count_images, count_getag