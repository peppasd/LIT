from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('authentification.urls')),
    path('projects/', include('projects.urls')),
    path('labeler/', include('labeler.urls'))
]
