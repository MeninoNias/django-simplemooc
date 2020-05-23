from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Course, Enrollment, Lesson
from .forms import ContatoCurso, CommentForm
from .decorators import enrollment_required

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

@login_required
def enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment, created = Enrollment.objects.get_or_create(user=request.user, course=course)

    if created:
        #enrollment.active()
        messages.success(request, 'Você foi inscrito no curso com sucesso')
    else:
        messages.info(request, 'Já esta inscrito no curso')


    return redirect('accounts:dash')

@login_required
def undo_enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment = get_object_or_404(
        Enrollment, user=request.user, course=course
    )
    if request.method == 'POST':
        enrollment.delete()
        messages.success(request, 'Sua inscrição foi cancelada com sucesso')
        return redirect('accounts:dash')
    template = 'courses/undo_enrollment.html'
    context = {
        'enrollment': enrollment,
        'course': course,
    }
    return render(request, template, context)

@login_required
@enrollment_required
def announcements(request, slug):
    course = request.course
    template = 'courses/announcements.html'
    context = {
        'course': course,
        'announcements': course.announcements.all()
    }
    return render(request, template, context)

@login_required
@enrollment_required
def show_announcements(request, slug, pk):
    template = 'courses/show_announcement.html'
    course = request.course
    announcements = get_object_or_404(course.announcements.all(), pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.announcement = announcements
            comment.save()
            form = CommentForm()
            messages.success(request, 'Seu comentário foi salvo')

    else:
        form = CommentForm()
    context = {
        'course': course,
        'announcement': announcements,
        'form': form
    }
    return render(request, template, context)

@login_required
@enrollment_required
def lessons(request, slug):
    template = 'courses/lessons.html'

    course = request.course
    lessons = course.release_lessons()

    if request.user.is_staff:
        lessons = course.lessons.all()

    context = {
        'course':course,
        'lessons': lessons
    }

    return render(request, template, context)

@login_required
@enrollment_required
def lesson(request, slug, pk):
    template = 'courses/lesson.html'

    course = request.course
    lesson = get_object_or_404(Lesson, pk=pk, course=course)

    if not request.user.is_staff and not lesson.is_available():
        messages.error(request, 'Aula não disponivel')
        return redirect('courses:lessons', slug=course.slug)

    context = {
        'course':course,
        'lesson':lesson
    }

    return render(request, template, context)