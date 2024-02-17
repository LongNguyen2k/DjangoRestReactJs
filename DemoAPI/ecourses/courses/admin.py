from django.contrib import admin
from django.contrib.auth.models import Permission
from django import forms
from django.db.models import Count
from django.template.response import TemplateResponse
from django.utils.html import mark_safe
from .models import Category, Lesson, Course, Tag, User
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonTagInLine(admin.StackedInline):
    model = Lesson.tags.through


class LessonAdmin(admin.ModelAdmin):

    class Media:
        css = {
            'all': ('/static/css/main.css', )
        }

    form = LessonForm
    list_display = ["id", "subject", "created_date", "active", "course"]
    search_fields = ["subject", "created_date", "course__subject"]
    list_filter = ["subject", "course__subject"]
    readonly_fields = ["avatar"]
    inlines = (LessonTagInLine, )

    def avatar(self, lesson):
        return mark_safe('''
            <image src='/static/{img_url}' alt='{alt}' width='120' />
            '''.format(img_url=lesson.image.name, alt=lesson.subject))


class LessonInline(admin.StackedInline):
    model = Lesson
    pk_name = 'course'


class CourseAdmin(admin.ModelAdmin):
    inlines = (LessonInline, )


class CourseAppAdminSite(admin.AdminSite):
    site_header = "He Thong Quan Ly Khoa Hoc"

    def get_urls(self):
        return [
            path('course-stats/', self.course_stats)
        ] + super().get_urls()

    def course_stats(self, request):
        course_count = Course.objects.count()
        stats = Course.objects.annotate(lesson_count=Count('lessons')).values("id", "subject", "lesson_count")

        return TemplateResponse(request, 'admin/course-stats.html', {
            'course_count': course_count,
            'stats': stats
        })


# admin_site = CourseAppAdminSite('mycourse')

# Register your models here.
admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)
admin.site.register(User)
admin.site.register(Permission)
# admin_site.register(Category)
# admin_site.register(Course, CourseAdmin)
# admin_site.register(Lesson, LessonAdmin)
# admin_site.register(Tag)