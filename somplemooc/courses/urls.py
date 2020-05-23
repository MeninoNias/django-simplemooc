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
    re_path(r'^(?P<slug>[\w_-]+)/inscricao-cancelamento/$', views.undo_enrollment, name='undo_enrollment'),
    re_path(r'^(?P<slug>[\w_-]+)/anuncios/$', views.announcements, name='announcements'),
    re_path(r'^(?P<slug>[\w_-]+)/anuncios/(?P<pk>\d+)/$', views.show_announcements, name='show_announcement'),
    re_path(r'^(?P<slug>[\w_-]+)/aulas/$', views.lessons, name='lessons'),
    re_path(r'^(?P<slug>[\w_-]+)/aulas/(?P<pk>\d+)/$', views.lesson, name='lesson'),
    re_path(r'^(?P<slug>[\w_-]+)/materiais/(?P<pk>\d+)/$', views.material, name='material'),
    ]