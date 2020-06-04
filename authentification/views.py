from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def register(request):
    return render(request, 'fronend/register.html')

def signin(request):
    return render(request, 'fronend/sign-in.html')

def resetpsw(request):
    return render(request, 'fronend/resetpsw.html')