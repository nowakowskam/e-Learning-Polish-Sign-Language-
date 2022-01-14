from django.db import models
from accounts.models import User
from django.db import models
from embed_video.fields import EmbedVideoField
from django.urls import reverse


class Lesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = EmbedVideoField(blank=True, null=True)
    name = models.CharField(max_length=80, verbose_name="Nazwa lekcji")
    auto_add = models.DateTimeField(auto_now_add=True)
    miniature = models.ImageField(upload_to="profile", default="lekcja.png", verbose_name="Miniatura")
    description = models.TextField(verbose_name="Opis", editable=True, default="", blank=True)
    course = models.CharField(max_length=80, verbose_name="Kurs", default="", blank=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('show_lesson', args=[str(self.id)])

class Test(models.Model):
    video = EmbedVideoField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, verbose_name="nazwa testu")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="tests", blank=True, verbose_name="Zdjęcie", default="")
    question = models.TextField(verbose_name="Pytanie", editable=True, default="" )
    option1 = models.CharField(max_length=200,null=True)
    option2 = models.CharField(max_length=200,null=True)
    option3 = models.CharField(max_length=200,null=True)
    option4 = models.CharField(max_length=200,null=True)
    answer = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.question

    def get_absolute_url(self):  # new
        return reverse('show_test', args=[str(self.id)])



# class Answear(models.Model):
#     test = models.ForeignKey(Test, on_delete=models.CASCADE)
#     is_correct = models.BooleanField("Correct answear", default=False)
#
#     def __str__(self):
#         return self.name


class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    tests = models.ManyToManyField(Test, through="TakenTest")


class Takentest(models.Model):
    learner = models.ForeignKey(
        Learner, on_delete=models.CASCADE, related_name="TakenTest"
    )
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="TakenTest")


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
