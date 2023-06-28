"""Defines urls patterns for users app"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    #Adding default urls
    path('', include('django.contrib.auth.urls')),
    #Register
    path('register/', views.register, name='register'),
]