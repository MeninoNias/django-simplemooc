from django.contrib import admin
from django.urls import path

from somplemooc.core import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contact, name='contact'),
    ]