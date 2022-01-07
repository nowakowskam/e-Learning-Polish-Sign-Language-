from django import forms
from .models import Lesson, Test, Answear, Learner, Takentest, Teacher


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = [
            "url",
            "name",
            "description",
            "miniature",
            "course",
        ]
    def clean(self):
        data = self.cleaned_data
        url = data.get('url')
        name = data.get('name')


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ["image", "name", "question"]
