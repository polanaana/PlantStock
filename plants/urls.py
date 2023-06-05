"""Defines new urls patterns for plants"""

from django.urls import path

from . import views

app_name = 'plants'
urlpatterns = [
    #Start screen
    path('', views.index, name='index'),
]
