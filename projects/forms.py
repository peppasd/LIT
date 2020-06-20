from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name','description','progress','created','labeled_photos','photos_total','users',]