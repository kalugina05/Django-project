from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('general_statistics', views.general_statistics),
]