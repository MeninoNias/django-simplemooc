from django.urls import include, path, re_path
from django.contrib.auth.views import LoginView, LogoutView

from somplemooc.accounts import views

app_name = 'accounts'

LoginView.template_name = 'accounts/login.html'
LogoutView.next_page = 'accounts:login'

urlpatterns = [
    path('', views.dash, name='dash'),
    path('entrar/', LoginView.as_view(), name='login'),
    path('sair/', LogoutView.as_view(), name='logout'),
    path('cadastro/', views.cadastroUser, name='register'),
    path('editar/', views.editarUser, name='edit'),
    path('editar-senha/', views.editarPassword, name='edit_password'),
    path('senha-reset/', views.senhaReset, name='password-reset'),
    re_path(r'^passoword-reset-confirm/(?P<key>\w+)/$', views.senhaConfirmReset, name='password-reset-confirm'),

]