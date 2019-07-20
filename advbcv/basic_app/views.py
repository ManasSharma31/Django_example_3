from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,TemplateView,ListView,DetailView,DeleteView
from . import models
from django.urls import reverse_lazy

# Create your views here.
class CBVIndex(TemplateView):
    template_name='index.html'


class SchoolList(ListView):
    model=models.School


class SchoolDetail(DetailView):
    model=models.School
    template_name='basic_app/school_detail.html'

class SchoolCreatview(CreateView):
    fields=('name','principal','address')
    model=models.School


class SchoolUpdate(UpdateView):
    fields=('name','principal')
    model=models.School


class SchoolDelete(DeleteView):
    context_object_name="schooldel"
    model=models.School
    success_url=reverse_lazy("basic_app:manas")
