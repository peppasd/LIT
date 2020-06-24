from django.urls import path
from . import views

urlpatterns = [
  path('', views.project_overview, name='project_overview'),
#  path('<int:project_id>', views.project_overview, name='project_overview'),

  path('images/', views.project_images, name='project_images')
]