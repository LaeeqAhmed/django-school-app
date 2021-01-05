from django.shortcuts import render

# Create your views here.
from .models import Enrollment
from .forms import EnrollmentForm
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView

class create(CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'Enrollments/create.html'
    success_url = '/Enrollment'


class listView(ListView):
    model = Enrollment
    template_name = 'Enrollments/listView.html'
    paginate_by = 5


class detailView(DetailView):
    model = Enrollment
    template_name = 'Enrollments/detailView.html'


class delete(DeleteView):
    model = Enrollment
    template_name = 'Enrollments/delete.html'
    success_url = '/Enrollment'


class update(UpdateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'Enrollments/update.html'
    success_url = '/Enrollment'
