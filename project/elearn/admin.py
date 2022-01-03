from django.contrib import admin
from .models import Lesson, Test, Answear, Learner, Takentest, Teacher
from embed_video.admin import AdminVideoMixin


class LessonVideo(AdminVideoMixin, admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Learner)
admin.site.register(Teacher)
admin.site.register(Lesson, LessonVideo)
admin.site.register(Answear)
admin.site.register(Takentest)
admin.site.register(Test)
