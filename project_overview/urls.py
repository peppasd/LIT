from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_overview, name='project_overview'),
  #  path('pictures/', views.about, name='pictures')
]