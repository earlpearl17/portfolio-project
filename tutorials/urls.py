from django.urls import path

from . import views

urlpatterns = [
    path('powershell/', views.powershell, name='powershell'),
    path('powershell/<int:tutorial_id>/', views.ps_tut, name='ps_tut'),
    path('scripting/', views.scripting, name='scripting'),
    path('network/', views.network, name='network'),
    path('misc/', views.misc, name='misc'),
]