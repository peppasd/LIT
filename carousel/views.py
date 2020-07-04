from django.shortcuts import render

# Create your views here.

def project_carousel(request):
    return render(request, 'project_carousel.html')
