from django.shortcuts import render
from .models import Project
from .forms import ProjectForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
import datetime

# Create your views here.

def overview(request):
    project_list = Project.objects.all()
    context = {
        'project_list': project_list,
    }
    return render(request, 'projects/overview.html', context=context)

def new_project(request):
    now = datetime.datetime.now()
    str = now.strftime('%Y-%m-%d')
    if request.method == "POST":
        form = ProjectForm(request.POST)        
        if form.is_valid():                 
            post = form.save(commit=False)                         
            #post.name = form.cleaned_data['name']
            #post.description = form.cleaned_data['description']
            #post.progress = form.cleaned_data['progress']
            #post.created = str
            #post.labeled_photos = form.cleaned_data['labeled_photos']
            #post.photos_total = form.cleaned_data['photos_total']              
            #post.labels = form.cleaned_data['labels']
            #post.users = form.cleaned_data['users']
            user_name = form.cleaned_data['user_tmp']
            post.save()
            post.users.add(User.objects.get(username=user_name))
            post.save()
            return HttpResponseRedirect('/projects/overview/')
    else:
        form = ProjectForm()
    return render(request, 'projects/new_project.html', {'form': form})

