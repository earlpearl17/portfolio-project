from django.urls import path

from . import views

urlpatterns = [
    path('', views.dev, name='dev'),
    #path('', views.home, name='dev'),
]