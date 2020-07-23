from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview, name='overview'),
    path('new_project/', views.new_project, name='new_project'),
    path('edit_project/<int:pk>/', views.edit_project, name='edit_project'),
    path('test/<int:pk>/', views.project_overview, name='project_overview'),
    path('test/images/', views.project_images, name='project_images'),
    path('upload_images/<int:pk>/', views.upload_images, name='upload_images'),
    path('project_images/<int:pk>/', views.project_images, name='project_images'),
    path('create_tags/<int:pk>/', views.create_tags, name='create_tags'),
    path('edit_tag/<int:pk>/', views.edit_tag, name='edit_tag'),
    path('removeImg/<slug:slug>/', views.removeImg, name='removeImg'),
    path('removeProject/<int:pk>/', views.removeProject, name='removeProject'),
]