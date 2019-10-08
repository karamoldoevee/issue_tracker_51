from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import IssueForm
from webapp.models import Issue
from django.core.paginator import Paginator




class IndexView(ListView):
    template_name = 'issue/index.html'

    context_object_name = 'issues'

    model = Issue

    ordering = ['-created_at']

    paginate_by = 5

    paginate_orphans = 1


class IssueView(DetailView):

    template_name = 'issue/issue.html'

    model = Issue


class IssueCreateView(CreateView):
    template_name = 'issue/create.html'

    model = Issue

    fields = ['summary', 'description', 'status', 'type']

    def get_success_url(self):
        return reverse('index')


class issue_update_view(UpdateView):
    model = Issue

    template_name = 'issue/update.html'

    fields = ['summary', 'description', 'status', 'type']

    context_object_name = 'issue'

    def get_success_url(self):
        return reverse('issue_view', kwargs={'pk': self.object.pk})

class issue_delete_view(DeleteView):

    template_name = 'issue/delete.html'

    model = Issue

    context_object_name = 'issue'

    success_url = reverse_lazy('index')








