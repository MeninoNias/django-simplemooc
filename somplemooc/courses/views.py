from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Course
from .forms import ContatoCurso

@login_required
def courses(request):

    cursos = Course.object.all()

    context = {
        'courses': cursos
    }

    template_name = 'courses/courses.html'
    return render(request, template_name, context)

@login_required
def details(request, slug):
    
    curso = get_object_or_404(Course, slug=slug)

    context = {
        'course': curso
    }

    template_name = 'courses/details.html'
    return render(request, template_name, context)

@login_required
def contatoCourse(request):

    context = {}

    if request.method == 'POST':
        form = ContatoCurso(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            print(form.cleaned_data)
            form.send_mail()
            form = ContatoCurso()
    else:
        form = ContatoCurso()

    context['form'] = form

    template_name = 'courses/contato_course.html'
    return render(request, template_name, context)
