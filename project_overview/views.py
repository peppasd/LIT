from django.shortcuts import render

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


# Create your views here.
def project_overview(request):
    context = {
        'projects': projects,
        'members': members
    }
    return render(request, 'project_overview.html', context)