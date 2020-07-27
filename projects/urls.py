from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview, name='overview'),
    path('new_project', views.new_project, name='new_project'),
    path('<int:pk>/edit_project', views.edit_project, name='edit_project'),
    path('<int:pk>/', views.project_overview, name='project_overview'),
    path('<int:pk>/upload_images', views.upload_images, name='upload_images'),
    path('<int:pk>/project_images', views.project_images, name='project_images'),
    path('<int:pk>/create_tags', views.create_tags, name='create_tags'),
    path('<int:pk>/edit_tag', views.edit_tag, name='edit_tag'),
    path('removeImg/<slug:slug>', views.removeImg, name='removeImg'),
    path('<int:pk>/removeProject', views.removeProject, name='removeProject'),
    path('<int:pk>/removeTag', views.removeTag, name='removeTag'),
    path('<int:pk>/download.json', views.download, name='download'),
]