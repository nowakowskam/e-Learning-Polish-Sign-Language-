from django.contrib import admin
from .models import Lesson, Test, Comment
from embed_video.admin import AdminVideoMixin


class LessonVideo(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Lesson, LessonVideo)
admin.site.register(Test)
admin.site.register(Comment)

