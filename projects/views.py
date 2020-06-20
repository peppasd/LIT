from django.shortcuts import render
from .models import Project
from .forms import ProjectForm

# Create your views here.

def overview(request):
    project_list = Project.objects.all()
    context = {
        'project_list': project_list,
    }
    return render(request, 'projects/overview.html', context=context)
