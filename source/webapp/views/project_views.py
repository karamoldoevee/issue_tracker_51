from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProjectForm
from webapp.models import Project
from django.core.paginator import Paginator




class ProjectIndexView(ListView):
    template_name = 'project/index.html'

    context_object_name = 'projects'

    model = Project

    ordering = ['-created_at']

    paginate_by = 5

    paginate_orphans = 1


class ProjectView(DetailView):

    template_name = 'project/project.html'

    model = Project


class ProjectCreateView(CreateView):
    template_name = 'project/create.html'

    model = Project

    fields = ['name']

    def get_success_url(self):
        return reverse('index')


class project_update_view(UpdateView):
    model = Project

    template_name = 'project/update.html'

    fields = ['name']

    context_object_name = 'name'

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})

class project_delete_view(DeleteView):

    template_name = 'project/delete.html'

    model = Project

    context_object_name = 'project'

    success_url = reverse_lazy('index')








