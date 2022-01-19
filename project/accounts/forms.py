from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile


class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileForm(forms.ModelForm):
    profile_photo = forms.ImageField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.CharField(required=False)
    birth_date = forms.DateField(label='Date of birth', widget=forms.SelectDateWidget())
    class Meta:
        model=Profile
        fields=[
        "profile_photo",
        "first_name",
        "last_name",
        "email",
        "birth_date",
        ]


