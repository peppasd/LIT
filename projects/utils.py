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
        ret.append(member.user)
    return ret


def allTags_project(project):
    ret = []
    tags = project.labels.all()
    for tag in tags:
        ret.append(tag)
    return ret
