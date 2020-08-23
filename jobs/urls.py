from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('powershell/', views.powershell, name='powershell'),
    path('scripting/', views.scripting, name='scripting'),
    path('network/', views.network, name='network'),
    path('misc/', views.misc, name='misc'),
]