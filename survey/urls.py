from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('questions', views.questions, name='questions'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('comments', views.comments, name='comments')
]
