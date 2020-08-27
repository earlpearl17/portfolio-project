from django.urls import path

from . import views

urlpatterns = [
    path('<int:topic_id>/', views.tutorials, name='tutorials'),
    path('<int:topic_id>/<int:tutorial_id>/', views.topic_tutorial, name='topic_tutorial'),
    path('<int:topic_id>/<int:tutorial_id>/<slug:slug>/', views.topic_tutorial, name='topic_tutorial_keywords'),
    
]