from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('survey/', include('survey.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]



