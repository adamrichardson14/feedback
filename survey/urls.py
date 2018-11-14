from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('questions', views.questions, name='questions'),
    path('dashboard', views.dashboard, name='dashboard')
]
