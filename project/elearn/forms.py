from django import forms
from .models import Lesson, Test, Comment
from accounts.models import User


class LessonForm(forms.ModelForm):

    miniature = forms.ImageField(required=False)
    url = forms.URLField(required=True)
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    # course= forms.ModelChoiceField(widget=forms.Select, queryset=Category.objects.none())
    class Meta:
        model = Lesson
        fields = [
            "url",
            "name",
            "description",
            "miniature",
            # "course",
        ]

    def __init__(self, *args, **kwargs):
        super(LessonForm, self).__init__(*args, **kwargs)
        self.fields["miniature"].label = "Miniaturka lekcji"
        self.fields["url"].label = "Adres internetowy do wideo"
        self.fields["name"].label = "Nazwa lekcji"
        self.fields["description"].label = "Opis"
        # self.fields['course'].label = "Kurs"


class TestCreateForm(forms.ModelForm):
    image = forms.ImageField(label="Zdjęcie do pytania", required=False)
    video = forms.URLField(label="Wideo do pytania", required=False)
    name = forms.CharField(label="Nazwa pytania")
    question = forms.CharField(label="Treść pytania")
    option1 = forms.CharField(label="Odpowiedz 1")
    option2 = forms.CharField(label="Odpowiedz 2")
    option3 = forms.CharField(label="Odpowiedz 3")
    option4 = forms.CharField(label="Odpowiedz 4")
    answer = forms.ChoiceField(
        label="Prawidłowa odpowiedź",
        choices=[
            ("option1", str(option1.label)),
            ("option2", str(option2.label)),
            ("option3", str(option3.label)),
            ("option4", str(option4.label)),
        ],
    )
    lesson = forms.ModelChoiceField(
        label="Przypisanie do lekcji",
        widget=forms.Select,
        queryset=Lesson.objects.none(),
    )

    class Meta:
        model = Test
        fields = [
            "image",
            "video",
            "name",
            "question",
            "option1",
            "option2",
            "option3",
            "option4",
            "answer",
            "lesson",
        ]

    def __init__(self, *args, **kwargs):
        test_owner = kwargs.pop("test_owner", None)
        owner = User.objects.filter(pk=test_owner.pk).first()
        super().__init__(*args, **kwargs)
        self.fields["lesson"].queryset = Lesson.objects.filter(user=owner)


class ShowTestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = [
            "image",
            "video",
            "name",
            "question",
            "option1",
            "option2",
            "option3",
            "option4",
            "answer",
            "lesson",
        ]


class CommentForm(forms.ModelForm):
    body = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={"name": "body", "rows": "4", "cols": "30"}),
    )

    class Meta:
        model = Comment
        fields = [
            "body",
        ]
        labels = {
            "body": "",
        }
