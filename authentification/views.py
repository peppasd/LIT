from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from .forms import UserCreationFormExtended, EditProfileForm, EditProfileFormInvalidEmail,UserCreationForm
from django.conf.urls import url
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse

# Create your views here.

def index(request):    
    return render(request, 'index.html')

def signup(request): 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/signup_done.html', {
                'form':form
            })
    else:
        form = UserCreationForm()   
    return render(request, 'registration/signup.html',{
        'form':form
    })

def login(request):    
    return render(request, 'login.html')

def logout(request):    
    return render(request, 'logout.html')

def logout_done(request):    
    return render(request, 'registration/logout_done.html')

def profile_edit(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return render(request,'registration/profile_edit_done.html', {
                'form':form
            })
        else:
            form = EditProfileFormInvalidEmail(instance=request.user)            
            return render(request, 'registration/profile_edit.html', {
            'form':form
        }) 
    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'registration/profile_edit.html', {
            'form':form
        })
