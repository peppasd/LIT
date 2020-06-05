from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register-page'),
    path('login', views.signin, name='signin-page'),
    path('recover', views.resetpsw, name='resetpsw-page'),
]