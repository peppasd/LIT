from django.shortcuts import render, get_object_or_404
from .models import Project, Photo, Member, Label, Value
from .forms import ProjectForm, LabelForm
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from .utils import existsUser, allUsers_project, allTags_project, getUser, calProgress
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def removeImg(request, slug):
    elm = Photo.objects.get(uuid=slug)
    project = elm.project
    elm.delete()
    return HttpResponseRedirect('/projects/project_images/{}/'.format(project.id))


@login_required
def removeProject(request, pk):
    elm = Project.objects.get(pk=pk)
    for member in elm.members.all():
        member.delete()    
    elm.delete()
    return HttpResponseRedirect('/projects/')


@login_required
def overview(request):
    project_list = []
    all_projects = []
    for project in Project.objects.all():
        x, y, z = calProgress(project)
        project.progress = x
        for member in project.members.all():
            if request.user == member.user.first():
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
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            post.owners.add(request.user)
            post.ownerName = request.user.username
            post.save()           
            return HttpResponseRedirect('/projects/')
    else:
        form = ProjectForm()
    return render(request, 'new_project.html', {'form': form})

@login_required
def edit_project(request, pk):
    context = {
            'pk': pk,
        }            
    post = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)            
            post.save()
            return HttpResponseRedirect('/projects/test/{}/'.format(pk))
    else:        
        form = ProjectForm(instance=post)
        context = {
            'pk': pk,
            'form': form,
        }        
    return render(request, 'edit_project.html', context)

@login_required
def removeTag(request, pk):
    elm = Label.objects.get(pk=pk)
    project = elm.project
    ok = True
    for value in Value.objects.all():
        if elm in value.label.all():
            ok = False
            break
    if ok:
        elm.delete()    
    return HttpResponseRedirect('/projects/test/{}/'.format(project.id))


@login_required
def edit_tag(request, pk):
    context = {
            'pk': pk,
    }
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
        context = {
            'pk': pk,
            'form': form,
        }        
    return render(request, 'edit_tag.html', context)

@login_required
def project_overview(request, pk):
    ph = ""
    project = Project.objects.get(id=pk)
    x, y, z = calProgress(project)
    project.progress = x
    if request.method == 'POST':
        username = request.POST['username']
        if username=='__join__':
            m = Member()
            m.save()
            m.user.add(request.user)
            m.save()
            project.members.add(m)
        else:
            if existsUser(username):
                project.owners.add(getUser(username))
            else:
                ph = "User {} does not exist".format(username)
            
    members = allUsers_project(project)
    tags = allTags_project(project)
    count_images = y
    tagged_images = z
    context = {
        'project': project,
        'members': members,
        'tags': tags,
        'count_images': count_images,
        'ph': ph,
        'tagged_images': tagged_images,
    }
    return render(request, 'project_overview.html', context)

@login_required
def project_images(request, pk):
    project = Project.objects.get(id=pk)
    context = {
        'project': project,
    }
    return render(request, 'project_images.html', context)


VALID_IMAGE_EXTENSIONS = [
    "jpg",
    "jpeg",
    "png",
]


@login_required
def upload_images(request, pk):
    context = {
            'pk': pk,            
    }
    if request.method == "GET":
        return render(request, 'upload_images.html', context)
    elif request.method == "POST":
        uploaded_file = request.FILES['img']
        extension = uploaded_file.name.split(".")[-1]
        if uploaded_file._size > settings.MAX_UPLOAD_SIZE:
            return HttpResponse("File too big.", status=413)
        elif extension not in VALID_IMAGE_EXTENSIONS:
            return HttpResponse("Invalid file extension.", status=415)
        else:
            obj = Photo(file=request.FILES['img'], name=uploaded_file.name, project=Project.objects.get(id=pk))
            obj.save()
            return HttpResponse("Upload successful.")


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
