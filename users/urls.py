"""Defines urls patterns for users app"""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    #Adding default urls
    path('', include('django.contrib.auth.urls')),
]