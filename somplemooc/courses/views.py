from django.shortcuts import render, get_object_or_404
from .models import Course
# Create your views here.

def courses(request):

    cursos = Course.object.all()

    context = {
        'courses': cursos
    }

    template_name = 'courses/courses.html'
    return render(request, template_name, context)


def details(request, pk):
    
    curso = get_object_or_404(Course, pk=pk)

    context = {
        'course': curso
    }

    template_name = 'courses/details.html'
    return render(request, template_name, context)