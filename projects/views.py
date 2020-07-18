from django.shortcuts import render
from .models import Project, Photo, Member
from .forms import ProjectForm, LabelForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
import datetime
from .utils import existsUser, allUsers_project, allTags_project, getUser
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage


# Create your views here.

@login_required
def overview(request):
    project_list = []
    all_projects = []
    for project in Project.objects.all():
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
def project_overview(request, pk):
    projects = []
    members = []
    tags = []
    images = []
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        username = request.POST['username']
        if username == '__join__':
            m = Member(user=request.user)
            m.save()
            project.members.add(m)
        else:
            if existsUser(username):
                project.owners.add(getUser(username))

    members = allUsers_project(project)
    tags = allTags_project(project)
    imgs = project.images.all()
    for img in imgs:
        images.append({'url': img.url})
    count_images = images.__len__
    tagged_images = 4

    context = {
        'project': project,
        'members': members,
        'images': images,
        'tags': tags,
        'count_images': count_images,
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
        images.append({'url': img.url})
    count_images = images.__len__
    tagged_images = 4
    context = {
        'project': project,
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
                url = fs.url(name)
                now = datetime.datetime.now()
                str = now.strftime('%Y-%m-%d')
                obj = Photo(created_at=str, title=name, name=name, url=url, project=Project.objects.get(id=pk))
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


