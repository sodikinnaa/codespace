from django.urls import path
from . import views

urlpatterns = [
    path('', views.homefunction, name='homefunction'),
    
]