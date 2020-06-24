from django.urls import path
from . import views

urlpatterns = [
    path('overview/', views.overview, name='overview'),
    path('new_project/', views.new_project, name='new_project'),
]