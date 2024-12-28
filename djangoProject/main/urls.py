from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('general_statistics', views.general_statistics),
    path('geography', views.geography),
    path('relevance', views.relevance),
    path('skills', views.skills),
    path('recent_jobs', views.recent_jobs),
]