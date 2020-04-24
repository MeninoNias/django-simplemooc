from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required

from somplemooc.core.util import generate_hash_key

from django.conf import settings

from .models import PasswordReset
from .forms import RegisterForm, EditarAccountForm, PasswordResetForm

User = get_user_model()

@login_required
def dash(request):
    template_name = 'accounts/dashboard.html'
    return render(request, template_name)

def cadastroUser(request):
    template_name = 'accounts/cadastro.html'
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username = user.username, password = form.cleaned_data['password1'])
            login(request, user)
            return redirect('core:home') 
    else:
        form = RegisterForm()
    context = {
        'form': form
    }

    return render(request, template_name, context)

def senhaReset(request):
    template_name = 'accounts/password-reset.html'
    context = {}

    form = PasswordResetForm(request.POST or None)

    if form.is_valid():
        user = User.objects.get(email=form.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)

@login_required
def editarUser(request):
    template_name = 'accounts/editar.html'
    
    context = {}
    if request.method == 'POST':
        form = EditarAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditarAccountForm(instance=request.user)
            context['success'] = True
    else:
        form = EditarAccountForm(instance=request.user)
    context['form'] = form

    return render(request, template_name, context)

def editarPassword(request):
    template_name = 'accounts/editar_password.html'
    context = {}

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form

    return render(request, template_name, context)
