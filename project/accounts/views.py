import profile

import requests

from .forms import UserRegisterForm
from django.conf import settings
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib import messages
from .forms import ProfileForm
from .models import User, Profile
from django.shortcuts import get_object_or_404, Http404

class SignUp(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/register.html'


    def form_valid(self, form):
        user=form.save()
        login(self.request, user)
        self.success_url = reverse_lazy('login')
        messages.success(self.request, 'Konto zostało zarejestrowane pomyślnie.')
        return super().form_valid(form)

class CreateProfileView(CreateView):
    form_class = ProfileForm
    template_name = 'accounts/create_profile.html'
    profile_exists = None

    def form_valid(self, form):
        form.instance.user_id=self.request.user.pk
        user = User.objects.filter(pk=self.request.user.pk).first()
        profile = Profile.objects.filter(user=user).first()
        self.success_url = reverse_lazy('show_profile')
        messages.success(self.request, 'Profil został założony.')
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(CreateProfileView, self).get_context_data(**kwargs)
        context['profile_exists']= Profile.objects.filter(
            user=User.objects.filter(
                pk=self.request.user.pk
            ).first())
        return context




class ShowProfileView(DetailView):
    model = Profile
    template_name = 'accounts/show_profile.html'

    def get_object(self):
        user = User.objects.filter(pk=self.request.user.pk).first()
        profile = Profile.objects.filter(user=user).first()

        return profile


class ProfileUpdateView(UpdateView):
    form_class = ProfileForm
    template_name = 'accounts/update_profile.html'
    model=Profile

    def form_valid(self, form):
        form.instance.user = User.objects.filter(pk=self.request.user.pk).first()
        form.save()
        self.success_url=reverse_lazy('show_profile')
        messages.success(self.request, 'Profil został zaktualizowany pomyślnie.')
        form.cleaned_data
        return super().form_valid(form)

