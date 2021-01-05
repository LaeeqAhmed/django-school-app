# Create your views here.
from .models import Student
from .forms import StudentForm
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView


class create(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/create.html'
    success_url = '/student'



class listView(ListView):
    model = Student
    template_name = 'students/listView.html'
    paginate_by = 5

class detailView(DetailView):
    model = Student
    template_name = 'students/detailView.html'


class delete(DeleteView):
    model = Student
    template_name = 'students/delete.html'
    success_url = '/student'



class update(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/update.html'
    success_url = '/student'
