from django.urls import path

from . import views

urlpatterns = [
    path('test/<int:pk>', views.project_labeler, name='project_labeler'),
]

