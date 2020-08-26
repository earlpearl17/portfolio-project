from django.urls import path

from . import views

urlpatterns = [
    path('<int:topic_id>/', views.tutorials, name='tutorials'),
    path('<int:topic_id>/<int:tutorial_id>/', views.topic_tutorial, name='topic_tutorial'),
    #path('<int:tutorial_id>/', views.topic_tutorial, name='topic_tutorial'),
    #path('<int:topic_id>/<int:tutorial_id>/', views.topic_tutorial, name='topic_tutorial'),
    #url(r'^categories/(?P<pk>\d+)/$', views.categories, name='categories'),
    # path('powershell/', views.powershell, name='powershell'),
    # path('powershell/<int:tutorial_id>/', views.ps_tut, name='ps_tut'),
    # path('scripting/', views.scripting, name='scripting'),
    # path('network/', views.network, name='network'),
    # path('misc/', views.misc, name='misc'),
]