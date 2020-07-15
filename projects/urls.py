from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview, name='overview'),
    path('new_project/', views.new_project, name='new_project'),
    path('test/', views.project_overview, name='project_overview'),
    #  path('<int:project_id>', views.project_overview, name='project_overview'),
    path('test/images/', views.project_images, name='project_images'),
]