from django.shortcuts import render
from .models import Project
from .forms import ProjectForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
import datetime
from .utils import existsUser
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def overview(request):
    project_list = Project.objects.all()
    context = {
        'project_list': project_list,
    }
    return render(request, 'projects/overview.html', context=context)

@login_required
def new_project(request):
    user_list = User.objects.all()
    txt = ''
    for user in user_list:
        txt += user.username + ', '
    context = {
        'txt': txt,
    }
    print(txt)
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
            return HttpResponseRedirect('/projects/overview/')
    else:
        form = ProjectForm()
    return render(request, 'projects/new_project.html', context=context)

