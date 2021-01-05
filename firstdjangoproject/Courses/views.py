from .models import Course
from .forms import CourseForm
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView


class create(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'Courses/create.html'
    success_url = '/course'


class listView(ListView):
    model = Course
    template_name = 'Courses/listView.html'
    paginate_by = 5

class detailView(DetailView):
    model = Course
    template_name = 'Courses/detailView.html'


class delete(DeleteView):
    model = Course
    template_name = 'Courses/delete.html'
    success_url = '/course'


class update(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'Courses/update.html'
    success_url = '/course'
