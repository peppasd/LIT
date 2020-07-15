from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('logout_done/', views.logout_done, name='logout_done'),
    path('signup/', views.signup, name='signup'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
]
