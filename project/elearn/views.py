from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.detail import BaseDetailView
from django_filters import FilterSet
from django.contrib import messages
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import LessonForm, TestForm

from django.shortcuts import get_object_or_404
from .models import Lesson, Test, Answear, Learner, Takentest, Teacher

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
    #form_class=LessonForm

    # def get_context_data(self, **kwargs):
    #     context = super(ShowLessonView, self).get_context_data(**kwargs)
    #     if 'form' not in context:
    #         context['form'] = self.form_class(instance=self.object)
    #     return self.reverse(context)
    #
    # def get_object(self):
    #     return get_object_or_404(Lesson, pk=1)
    # context_object_name='item'

    # def get(self, request, *args, **kwargs):
    #     pk = self.kwargs['item_pk']
    #     obiekcik = get_object_or_404(Lesson, pk=pk)
    #     context = {'obiekcik': obiekcik}
    #     print(obiekcik,"XDDDDDDDDDDDDDDDDDDDDDDDDDDdd")
    #     return render(reverse('show_lesson', kwargs={'pk':pk}))
        # return reverse_lazy('show_lesson', kwargs={'obiekcik': obiekcik})
        # return obiekcik
    #
    # def get(self, request, *args, **kwargs):
    #     context = super(ShowLessonView, self).get_context_data(*args, **kwargs)
    #
    #     pk = self.kwargs['item_pk']
    #     print("XDDDDDDDDDDDDDDDDDDd", pk)
    #
    #     obiekcik = get_object_or_404(Lesson, pk=pk)
    #     context["obiecik"] = obiekcik
    #     return obiekcik

    # def get_context_data(self, *args, **kwargs):
        # if 'form_lesson' not in context:
        #     context['form_ticket'] = self.form_class(instance=self.object)

        # return context

    def get_success_url(self, item):  # noqa: D102
        pk = self.item.pk
        return reverse_lazy('show_lesson', kwargs={'pk': pk})

# class ShowLessonView(FormView):
#     template_name = 'elearn/show_lesson.html'
#     form_class = LessonForm
#     model = Lesson
#
#     def get_success_url(self, request, *args, **kwargs):  # noqa: D102
#         qs=get_object_or_404(Lesson, pk=Lesson.pk)
#         self.success_url=reverse_lazy('show_lesson', kwargs={'pk': qs})

class CreateTestView(CreateView):
    form_class = TestForm
    template_name ='elearn/create_test.html'

    def form_valid(self, form):
        form.save()
        self.success_url=reverse_lazy('show_created_test', kwargs={'pk': form.instance.id})
        messages.success(self.request, 'Test Created succesfully.')
        return super().form_valid(form)

# zmien lekcje
class UpdateLessonView(UpdateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'elearn/update_lesson.html'

    def get_context_data(self, **kwargs):  # noqa: D102
        context = super(UpdateLessonView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(instance=self.object)
    # def get_success_url(self):  # noqa: D102
    #     pk = self.object.id
    #     return reverse_lazy('update_lesson', kwargs={'pk': pk})
# pokazliste lekcji
class ListLessonView(ListView):
    paginate_by = 5
    model = Lesson
    template_name = 'elearn/list_lesson.html'

    def get_success_url(self):  # noqa: D102
        qs=self.model.objects.all()
        return qs

# utworz test
# zmien test
# pokaz testy

def index(request):
    dane = {'title' : 'About'}
    return render(request, 'base.html',dane)