from django.contrib import admin
from django.urls import path, re_path

from somplemooc.courses import views

app_name = 'courses'
urlpatterns = [
    path('', views.courses, name='courses'),
    re_path(r'^(?P<pk>\d+)/$', views.details, name='details'),
    ]