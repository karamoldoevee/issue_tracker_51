from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProjectForm, SimpleSearchForm
from webapp.models import Project
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.http import urlencode




class ProjectIndexView(ListView):
    template_name = 'project/index.html'

    context_object_name = 'projects'

    model = Project

    ordering = ['created_at']

    paginate_by = 5

    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()

        self.search_value = self.get_search_value()

        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        context['form'] = self.form

        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})

        return context

    def get_queryset(self):

        queryset = super().get_queryset()

        if self.search_value:
            query = Q(name__icontains=self.search_value)

            queryset = queryset.filter(query)

        return queryset

    def get_search_form(self):

        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):

        if self.form.is_valid():
            return self.form.cleaned_data['search']

        return None


class ProjectView(DetailView):

    template_name = 'project/project.html'

    model = Project


class ProjectCreateView(CreateView):
    template_name = 'project/create.html'

    model = Project

    fields = ['name', 'description']

    def get_success_url(self):
        return reverse('project_index')


class project_update_view(UpdateView):
    model = Project

    template_name = 'project/update.html'

    fields = ['name', 'description']

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})

class project_delete_view(DeleteView):

    template_name = 'project/delete.html'

    model = Project

    context_object_name = 'project'

    success_url = reverse_lazy('project_index')








