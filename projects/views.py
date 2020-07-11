from django.shortcuts import render
from .models import Project
from .forms import ProjectForm, LabelForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
import datetime
from .utils import existsUser, allUsers_project, allTags_project
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def overview(request):
    project_list = Project.objects.all()
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
            post.save()
            post.owners.add(request.user)
            post.save()            
            return HttpResponseRedirect('/projects/')
    else:
        form = ProjectForm()
    return render(request, 'new_project.html', {'form': form})


# Dummy Project
projects = []
members = []
tags = []
images = [
    {'url': 'https://www.cheatsheet.com/wp-content/uploads/2017/12/Queen-Elizabeth-Waving.jpg',
     'isTagged': True, },
    {'url': 'https://images-na.ssl-images-amazon.com/images/I/C1YRnQIzuTS._SL1000_.png',
     'isTagged': False, },
    {
        'url': 'http://i.dailymail.co.uk/i/newpix/2018/06/29/21/4DBC9DE400000578-0-Fans_of_the_Royal_family_grew_worried_about_Queen_Elizabeth_II_s-m-55_1530303342340.jpg',
        'isTagged': False, },
    {'url': 'https://tse3.mm.bing.net/th?id=OIP.raEAx7WtuS2iOyrYhTQUdQHaE8&pid=Api',
     'isTagged': True, },
    {'url': 'https://www.swr.de/-/id=22651064/property=full/1jzbpoi/Queen%201985.jpg',
     'isTagged': True},
    {'url': 'https://tse1.mm.bing.net/th?id=OIP.HC7u7SXAjRSapw29hIQ6ZgHaFj&pid=Api',
     'isTagged': True, },
]
count_images = images.__len__
tagged_images = 4

# Create your views here.
@login_required
def project_overview(request,pk):
    project = Project.objects.get(id=pk)
    members = allUsers_project(project)
    tags = allTags_project(project)

    context = {
        'project':project,        
        'members': members,
        'images': [images[0], images[1], images[2]],
        'tags': tags,
        'count_images': count_images,
    }
    # project = get_object_or_404(Project, pk=project_id)
    return render(request, 'project_overview.html', context)


@login_required
def project_images(request):
    context = {
        'projects': projects,
        'members': members,
        'images': images,
        'tags': tags
    }
    return render(request, 'project_images.html', context)

@login_required
def upload_images(request):
    return render(request, 'upload_images.html')

@login_required
def create_tags(request, pk): 
    context = {
            'pk': pk,            
        } 
    if request.method == "POST":
        form = LabelForm(request.POST)       
        if form.is_valid():            
            post = form.save(commit=False)                        
            post.save()
            post.project = Project.objects.get(id=pk) 
            post.save()
            txt = '/projects/test/{}/'.format(pk)                     
            return HttpResponseRedirect(txt)
    else:
        form = LabelForm()
        context = {
            'pk': pk,
            'form': form,
        }        
    return render(request, 'create_tags.html', context) 

    
