from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('general_statistics', views.general_statistics, name='general_statistics'),
    path('relevance', views.relevance, name='relevance'),
    path('geography', views.geography, name='geography'),
    path('skills', views.skills, name='skills'),
    path('recent_jobs', views.recent_jobs, name='recent_jobs'),
]