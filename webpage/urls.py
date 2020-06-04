from django.urls import path
from . import views


urlpatterns = [
    path('', views.register, name='register-page'),
    path('', views.signin, name='signin-page'),
    path('', views.resetpsw, name='resetpsw-page'),
]
