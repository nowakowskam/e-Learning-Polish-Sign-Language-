from django.db import models
from accounts.models import User
from django.db import models
from embed_video.fields import EmbedVideoField
from django.urls import reverse

# class Category(models.Model):
#     name = models.CharField(max_length=80, verbose_name="Kurs", default="", blank=True, null=True)

class Lesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = EmbedVideoField(blank=True, null=True)
    name = models.CharField(max_length=80, verbose_name="Nazwa lekcji")
    create_date = models.DateTimeField(auto_now_add=True)
    miniature = models.ImageField(upload_to="", default="lekcja.png", verbose_name="Miniatura")
    description = models.TextField(verbose_name="Opis", editable=True, default="", blank=True)
    # course = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('show_lesson', args=[str(self.id)])

    class Meta:
        ordering = ['create_date']
        verbose_name = "Lekcja"
        verbose_name_plural = "Lekcje"




class Test(models.Model):
    video = EmbedVideoField(blank=True, null=True, verbose_name="wideo")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="użytkownik")
    name = models.CharField(max_length=80, verbose_name="nazwa testu")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="tests", blank=True, verbose_name="Zdjęcie", default="")
    question = models.TextField(verbose_name="Pytanie", editable=True, default="" )
    option1 = models.CharField(max_length=200,null=True, verbose_name="Odpowiedz 1")
    option2 = models.CharField(max_length=200,null=True,verbose_name="Odpowiedz 2")
    option3 = models.CharField(max_length=200,null=True, verbose_name="Odpowiedz 3")
    option4 = models.CharField(max_length=200,null=True, verbose_name="Odpowiedz 4")
    answer = models.CharField(max_length=200,null=True, verbose_name="Poprawna odpowiedź")

    def __str__(self):
        return self.question

    def get_absolute_url(self):  # new
        return reverse('show_test', args=[str(self.id)])
    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Testy"

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="użytkownik" )
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="data dodania")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="lekcja")
    body = models.TextField(max_length=512, verbose_name="komentarz")

    class Meta:
        ordering = ['create_date']

    def __str__(self) -> str:  # noqa: D105
        return f'ID{self.id}:Lesson-{self.lesson.id}:{self.owner}'

    class Meta:
        verbose_name = "Komentarz"
        verbose_name_plural = "Komentarze"
