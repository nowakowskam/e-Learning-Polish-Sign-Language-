from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_learner = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to=".", default="default_profile.jpg")
    first_name = models.CharField(max_length=80, default="")
    last_name = models.CharField(max_length=80, default="")
    email = models.EmailField(default="")
    birth_date = models.DateField(default="2000-01-01")
    bio = models.CharField(max_length=255, default="")
    def __str__(self):
        return self.user.username
