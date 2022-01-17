from .forms import UserRegisterForm
from django.conf import settings
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib import messages

class SignUp(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        user=form.save()
        login(self.request, user)
        self.success_url = reverse_lazy('index')
        messages.success(self.request, 'Witaj')
        return super().form_valid(form)