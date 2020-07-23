from django.shortcuts import render, get_object_or_404
from .models import Project, Photo, Member, Label
from .forms import ProjectForm, LabelForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
import datetime
from .utils import existsUser, allUsers_project, allTags_project, getUser, calProgress
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage





# Create your views here.

@login_required
def removeImg(request, slug):
    elm = Photo.objects.get(uuid=slug)
    project = elm.project
    #fs = FileSystemStorage()
    #fs.delete(elm.name)
    elm.delete()
    return HttpResponseRedirect('/projects/project_images/{}/'.format(project.id))

@login_required
def overview(request):
    project_list = []
    all_projects = []
    for project in Project.objects.all():
        x, y, z = calProgress(project)
        project.progress = x
        for member in project.members.all():
            if request.user == member.user:
                project_list.append(project)
        if request.user in project.owners.all():
            if project not in project_list:
                project_list.append(project)

    for project in Project.objects.all():
        if project not in project_list:
            all_projects.append(project)

    context = {
        'project_list': project_list,
        'all_projects': all_projects,
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
def edit_project(request, pk):
    post = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)            
            post.save()
            return HttpResponseRedirect('/projects/test/{}/'.format(pk))
    else:
        form = ProjectForm(instance=post)
    return render(request, 'edit_project.html', {'form': form})


@login_required
def edit_tag(request, pk):
    post = get_object_or_404(Label, pk=pk)
    project = post.project
    if request.method == "POST":
        form = LabelForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)            
            post.save()
            return HttpResponseRedirect('/projects/test/{}/'.format(project.id))
    else:
        form = LabelForm(instance=post)
    return render(request, 'edit_tag.html', {'form': form})

@login_required
def project_overview(request,pk):    
    projects = []
    members = []
    tags = []
    images = []
    ph = ""

    project = Project.objects.get(id=pk)
    x,y,z = calProgress(project)
    project.progress = x
    if request.method == 'POST':
        username = request.POST['username']
        if username=='__join__':
            m = Member(user=request.user)
            m.save()
            project.members.add(m)
        else:
            if existsUser(username):
                project.owners.add(getUser(username))
            else:
                ph = "User {} does not exist".format(username)
            
    members = allUsers_project(project)
    tags = allTags_project(project)
    imgs = project.images.all()
    for img in imgs:
        images.append(img)
    count_images = y
    tagged_images = z

    context = {
        'project':project,        
        'members': members,
        'images': images,
        'tags': tags,
        'count_images': count_images,
        'ph' : ph,
        'tagged_images': tagged_images,
    }
    # project = get_object_or_404(Project, pk=project_id)
    return render(request, 'project_overview.html', context)


@login_required
def project_images(request, pk):
    projects = []
    members = []
    tags = []
    images = []
    project = Project.objects.get(id=pk)
    members = allUsers_project(project)
    tags = allTags_project(project)
    imgs = project.images.all()
    for img in imgs:
        images.append(img)
    count_images = images.__len__
    tagged_images = 4
    context = {
        'project':project,        
        'members': members,
        'images': images,
        'tags': tags,
        'count_images': count_images,
    }
    return render(request, 'project_images.html', context)


VALID_IMAGE_EXTENSIONS = [
    "jpg",
    "jpeg",
    "png",
    "gif",
]


@login_required
def upload_images(request, pk):
    context = {
            'pk': pk,            
        } 
            
    if request.method == "POST":
        uploaded_files = request.FILES.getlist('img')
        for uploaded_file in uploaded_files:
            ends = uploaded_file.name.split(".")
            end = ends[1]           
            if VALID_IMAGE_EXTENSIONS.count(end) > 0:
                fs = FileSystemStorage()
                name = fs.save(uploaded_file.name, uploaded_file)
                now = datetime.datetime.now()
                str = now.strftime('%Y-%m-%d') 
                obj = Photo(created_at=str,name=name,project=Project.objects.get(id=pk))
                obj.save() 
                obj.file.save(name,fs.open(name))                
                obj.save() 
                fs.delete(name)                               
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

    
