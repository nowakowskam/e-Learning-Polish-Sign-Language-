from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic.detail import BaseDetailView
from django_filters import FilterSet
from django import http
from django.contrib import messages
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from .forms import LessonForm, TestCreateForm, ShowTestForm
from accounts.models import User


from django.shortcuts import get_object_or_404
from .models import Lesson, Test, Learner, Takentest, Teacher

# Create your views here.
# utworz lekcje
class CreateLessonView(CreateView):
    form_class = LessonForm or None
    template_name ='elearn/create_lesson.html'

    def form_valid(self, form):
        form.instance.user_id=self.request.user.pk

        form.save()
        self.success_url=reverse_lazy('create_lesson', kwargs={'pk': form.instance.id})
        messages.success(self.request, 'Lesson Created succesfully.')
        form.cleaned_data
        return super().form_valid(form)

class ShowLessonView(DetailView):
    model = Lesson
    template_name = 'elearn/show_lesson.html'

    def get_context_data(self, **kwargs):
        context = super(ShowLessonView, self).get_context_data(**kwargs)
        lesson = Lesson.objects.filter(pk=self.object.pk)
        context['lesson'] = lesson

        return context

    # def get_success_url(self, item):  # noqa: D102
    #     pk = self.item.pk
    #     return reverse_lazy('show_lesson', kwargs={'pk': pk})




class UpdateLessonView(UpdateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'elearn/update_lesson.html'

    # def get_context_data(self, **kwargs):
    #     context = super(UpdateLessonView, self).get_context_data(**kwargs)
    #     form = Lesson.objects.filter(pk=self.object.pk)
    #     context['form'] = form

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Zmiany zostały zapisane.')
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):  # noqa: D102
    #     context = super(UpdateLessonView, self).get_context_data(**kwargs)
    #     if 'form' not in context:
    #         context['form'] = self.form_class(instance=self.object)
    # def get_success_url(self,pk):  # noqa: D102
    #     pk = self.object.id
    #     return reverse_lazy('update_lesson', kwargs={'pk': self.object.pk})

# pokazliste lekcji
class ListLessonView(ListView):
    paginate_by = 5
    model = Lesson
    template_name = 'elearn/list_lesson.html'

    def get_success_url(self):  # noqa: D102
        qs=self.model.objects.all()
        return qs

class LessonDeleteView(DeleteView):
    model = Lesson
    success_url = reverse_lazy('/elearn/delete_lesson/')


# utworz test


class CreateTestView(CreateView):
    form_class = TestCreateForm
    template_name ='elearn/create_test.html'

    def form_valid(self, form):
        #TODO tutaj powinno byc owner albo owner_id
        form.instance.owner = User.objects.filter(pk=self.request.user.pk).first()
        if form.instance.answer == 'option1':
            form.instance.answer = form.instance.option1
        if form.instance.answer == 'option2':
            form.instance.answer = form.instance.option2
        if form.instance.answer == 'option3':
            form.instance.answer = form.instance.option3
        else:
            form.instance.answer = form.instance.option4

        form.save()
        self.success_url=reverse_lazy('test_list')
        messages.success(self.request, 'Pomyślnie utworzono test')
        return super().form_valid(form)

    def get_form_kwargs(self):  # noqa: D102
        kwargs = super().get_form_kwargs()
        kwargs.update(
            {
                'test_owner': self.request.user,
            },
        )
        return kwargs



class TestListView(ListView):
    template_name = 'test_list'
    paginate_by = 5
    model = Test
    def get_success_url(self):  # noqa: D102
        qs=self.model.objects.all()
        return qs






# zmien test
class UpdateTestView(UpdateView):
    model = Test
    form_class = ShowTestForm
    template_name = 'elearn/update_test.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Zmiany zostały zapisane.')
        return super().form_valid(form)

# pokaz testy
class DeleteTestView(DeleteView):
    model = Test
    template_name = 'elearn/test_confirm_delete.html'
    form = TestCreateForm
    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Test, pk = pk)

    def get_success_url(self):
        return reverse('test_list')

    def delete(self, request, *args, **kwargs):
            self.object = self.get_object()
            if self.object.owner == request.user:
                success_url = self.get_success_url()
                self.object.delete()
                return http.HttpResponseRedirect(success_url)
            else:
                return http.HttpResponseForbidden("Możesz usunać tylko swoją lekcje")



class ShowTestView(DetailView):
    model = Test
    template_name = 'elearn/show_test.html'

    # def get_context_data(self, **kwargs):
    #     context = super(ShowTestView, self).get_context_data(**kwargs)
    #     test = Test.objects.filter(pk=self.object.pk)
    #     context['test'] = test
    #
    #     return context


def index(request):
    dane = {'title' : 'About'}
    return render(request, 'base.html',dane)