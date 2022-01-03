from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django_filters import FilterSet
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import LessonForm, TestForm
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

class ShowCreatedLessonView(UpdateView):
    pass

class CreateTestView(CreateView):
    form_class = TestForm
    template_name ='elearn/create_test.html'

    def form_valid(self, form):
        form.save()
        self.success_url=reverse_lazy('show_created_test', kwargs={'pk': form.instance.id})
        messages.success(self.request, 'Test Created succesfully.')
        return super().form_valid(form)

# zmien lekcje
# pokazliste lekcji
class ListLessonView(ListView):
    paginate_by = 5
    model = Lesson
    template_name = 'elearn/list_lesson.html'

    def get_queryset(self):  # noqa: D102
        qs=self.model.objects.all()
        return qs
# utworz test
# zmien test
# pokaz testy

def index(request):
    dane = {'title' : 'About'}
    return render(request, 'base.html',dane)