from django.contrib import admin
from .models import Project
from .models import Photo

# Register your models here.

admin.site.register(Project)
admin.site.register(Photo)