from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_learner = models.BooleanField(default=True, verbose_name='uczen')
    is_teacher = models.BooleanField(default=False, verbose_name='nauczyciel')
    is_admin = models.BooleanField(default=False, verbose_name='admin')

    class Meta:
        verbose_name = "Użytkownik"
        verbose_name_plural = "Użytkownicy"


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

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profile"
