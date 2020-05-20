from django.contrib import admin
from .models import Course, Annoucement, Comment, Enrollment, Lesson, Material


# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at']

    prepopulated_fields = {'slug': ('name',) }

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'status', 'created_at']

class AnnoucementAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'created_at']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user',  'created_at']


admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Annoucement, AnnoucementAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Lesson)
admin.site.register(Material)

