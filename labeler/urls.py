from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>', views.project_labeler, name='project_labeler'),
]

