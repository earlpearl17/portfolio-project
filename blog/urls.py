from django.urls import path

from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    # Match urls based on ID + keywords
    path("<int:blog_id>/<slug:slug>", views.detail, name="detail-keywords"),
]
