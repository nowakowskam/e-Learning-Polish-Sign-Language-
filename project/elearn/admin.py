from django.contrib import admin
from .models import Lesson, Test, Comment
# from .models import Category
from embed_video.admin import AdminVideoMixin


class LessonVideo(AdminVideoMixin, admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Lesson, LessonVideo)
admin.site.register(Test)
admin.site.register(Comment)
# admin.site.register(Category)