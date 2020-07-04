from django.urls import path

from . import views

urlpatterns = [
    path('', views.project_carousel, name='project_caaaarousel'),
]

