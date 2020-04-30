from django.contrib import admin
from django.urls import path, re_path

from somplemooc.courses import views

app_name = 'courses'
urlpatterns = [
    path('', views.courses, name='courses'),
    path('contato_course/', views.contatoCourse, name='contato_course'),
    #re_path(r'^(?P<pk>\d+)/$', views.details, name='details'),
    re_path(r'^(?P<slug>[\w_-]+)/$', views.details, name='details'),
    re_path(r'^(?P<slug>[\w_-]+)/inscricao/$', views.enrollment, name='enrollment'),
    ]