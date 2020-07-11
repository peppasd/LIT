from django.forms import ModelForm
from .models import Project, Label

class ProjectForm(ModelForm):
    class Meta:
        model = Project        
        fields = ['name','description']

class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = ['name', 'type']
        