from django.contrib.auth.models import User
from .models import Project

def existsUser(username):
    if User.objects.filter(username=username).exists():
        return True
    
    return False

def allProjects_user(username):
    ret = []
    projects = Project.objects.all()
    for project in projects:
        users = project.users.objects.all()
        for elm in users:
            if elm.username == username:
                ret.append(project)    
    return ret