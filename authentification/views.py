from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationFormExtended

# Create your views here.

def index(request):    
    return render(request, 'index.html')

def signup(request): 
    if request.method == 'POST':
        form = UserCreationFormExtended(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationFormExtended()   
    return render(request, 'registration/signup.html',{
        'form':form
    })

def login(request):    
    return render(request, 'login.html')

def logout(request):    
    return render(request, 'logout.html')
