from django.shortcuts import render
from .models import Project, Photo
from .forms import ProjectForm, LabelForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
import datetime
from .utils import existsUser, allUsers_project, allTags_project
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage



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



@login_required
def project_overview(request,pk):
    projects = []
    members = []
    tags = []
    images = []
    project = Project.objects.get(id=pk)
    members = allUsers_project(project)
    tags = allTags_project(project)
    imgs = project.images.all()
    for img in imgs:
        images.append({'url':img.url})
    count_images = images.__len__
    tagged_images = 4

    context = {
        'project':project,        
        'members': members,
        'images': images,
        'tags': tags,
        'count_images': count_images,
    }
    # project = get_object_or_404(Project, pk=project_id)
    return render(request, 'project_overview.html', context)


@login_required
def project_images(request):
    projects = []
    members = []
    tags = []
    images = []
    context = {
        'projects': projects,
        'members': members,
        'images': images,
        'tags': tags
    }
    return render(request, 'project_images.html', context)

@login_required
def upload_images(request, pk):
    context = {
            'pk': pk,            
        } 
    
    if request.method == "POST":
        uploaded_file = request.FILES['img']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        now = datetime.datetime.now()
        str = now.strftime('%Y-%m-%d')
        obj = Photo(created_at=str,title=name,name=name,url=url,project=Project.objects.get(id=pk))
        obj.save()
    return render(request, 'upload_images.html', context)

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

    
