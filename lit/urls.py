from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('authentification.urls')),
    path('projects/', include('projects.urls')),
    #AWS s3
    path('s3direct/', include('s3direct.urls')),
]
