from django.template import Library

from somplemooc.courses.models import Enrollment

register = Library()

@register.inclusion_tag('courses/templatetags/my_courses.html')
def my_courses(user):
    enrollment = Enrollment.objects.filter(user=user)
    context = {
        'enrollments': enrollment
    }

    return context

@register.simple_tag()
def load_my_courses(user):
    return  Enrollment.objects.filter(user=user)