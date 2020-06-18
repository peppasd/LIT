from django.shortcuts import render

#Dummy Project
projects = [
    {
        'title' : 'Face Detector',
        'members': 'John, Big John, Raw John',
        'date_created': 'August 22, 2030'
    },
    
    {
        'title' : 'Puppy Detector',
        'members': 'Pop, Big Pop, Raw Pop',
        'date_created': 'November 02, 1894'
    }
]


# Create your views here.
def project_overview(request):
    context = {
        'projects': projects
    }
    return render(request, 'project_overview.html', context)