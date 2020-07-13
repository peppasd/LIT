from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview, name='overview'),
    path('new_project/', views.new_project, name='new_project'),
    path('test/<int:pk>/', views.project_overview, name='project_overview'),
    #  path('<int:project_id>', views.project_overview, name='project_overview'),
    path('test/images/', views.project_images, name='project_images'),
    path('upload_images/<int:pk>/', views.upload_images, name='upload_images'),
    path('project_images/<int:pk>/', views.project_images, name='project_images'),
    path('create_tags/<int:pk>/', views.create_tags, name='create_tags')
]