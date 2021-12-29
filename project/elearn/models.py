from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from embed_video.fields import EmbedVideoField


class User(AbstractUser):
    is_learner = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='', default='logo.jpg')
    first_name = models.CharField(max_length=80, default='')
    last_name = models.CharField(max_length=80, default='')
    email = models.EmailField(default='')
    birth_date = models.DateField(default='2000-01-01')
    country = models.CharField(max_length=80, default='')

    def __str__(self):
        return self.user.username


class Lesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = EmbedVideoField(blank=True, null=True)
    name = models.CharField(max_length=80)
    auto_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    # class Meta:
    #     ordering=['-auto_add']


class Test(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    # TODO description


class Answear(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    is_correct = models.BooleanField("Correct answear", default=False)

    def __str__(self):
        return self.name


class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    tests = models.ManyToManyField(Test, through='TakenTest')


class Takentest(models.Model):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE, related_name="TakenTest")
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="TakenTest")


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)