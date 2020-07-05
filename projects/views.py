from django.shortcuts import render
from .models import Project
from .forms import ProjectForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
import datetime
from .utils import existsUser, allProjects_user
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def overview(request):
    project_list = allProjects_user(request.user.username)
    context = {
        'project_list': project_list,
    }
    return render(request, 'overview.html', context=context)

@login_required
def new_project(request):    
    now = datetime.datetime.now()
    str = now.strftime('%Y-%m-%d')
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():                 
            post = form.save(commit=False)  
            post.created = str          
            user_name = form.cleaned_data['user_tmp']
            user_names = user_name.split(', ')
            post.save()
            post.users.add(request.user)
            post.save()
            for user in user_names:
                if existsUser(user):
                    post.users.add(User.objects.get(username=user))                
                post.save()
            return HttpResponseRedirect('/projects/')
    else:
        form = ProjectForm()
    return render(request, 'new_project.html', {'form':form})

#Dummy Project
projects = [
    {
        'id' : '001',
        'title' : 'Face Detector',
        'date_created': 'August 22, 2030'
    },
    
    {
        'id': '002',
        'title' : 'Puppy Detector',
        'date_created': 'November 02, 1894'
    }
]
members = [
    {
       'username': 'John'
    },
    {
       'username': 'Big John'
    },
    {
       'username': 'Raw John'
    }
]
tags = [
    'band',
    'the queen',
    'old'
]
images = [
    {'url':'https://www.cheatsheet.com/wp-content/uploads/2017/12/Queen-Elizabeth-Waving.jpg',
     'isTagged': True,},
    {'url':'https://images-na.ssl-images-amazon.com/images/I/C1YRnQIzuTS._SL1000_.png',
    'isTagged': False,},
    {'url':'http://i.dailymail.co.uk/i/newpix/2018/06/29/21/4DBC9DE400000578-0-Fans_of_the_Royal_family_grew_worried_about_Queen_Elizabeth_II_s-m-55_1530303342340.jpg',
    'isTagged': False,},
    {'url':'https://tse3.mm.bing.net/th?id=OIP.raEAx7WtuS2iOyrYhTQUdQHaE8&pid=Api',
    'isTagged':True,},
    {'url':'https://www.swr.de/-/id=22651064/property=full/1jzbpoi/Queen%201985.jpg',
    'isTagged':True},
    {'url':'https://tse1.mm.bing.net/th?id=OIP.HC7u7SXAjRSapw29hIQ6ZgHaFj&pid=Api',
    'isTagged':True,},
]
count_images = images.__len__
tagged_images = 4

# Create your views here.
@login_required
def project_overview(request):
    context = {
        'projects': projects,
        'members': members,
        'images': [images[0],images[1],images[2]],
        'tags':tags,
        'count_images': count_images,
    }
    #project = get_object_or_404(Project, pk=project_id)
    return render(request, 'project_overview.html', context)


@login_required
def project_images(request):
    context = {
        'projects': projects,
        'members': members,
        'images':images,
        'tags':tags
    }
    return render(request, 'project_images.html', context)

def upload_images(request):
    return render(request, 'upload_images.html')

def create_tags(request):
    return render(request, 'create_tags.html')
