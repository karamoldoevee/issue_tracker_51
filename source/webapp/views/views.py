from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import IssueForm, SimpleSearchForm
from webapp.models import Issue
from django.core.paginator import Paginator
from django.db.models import Q

from django.utils.http import urlencode




class IndexView(ListView):
    template_name = 'issue/index.html'

    context_object_name = 'issues'

    model = Issue

    ordering = ['-created_at']

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
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)

            queryset = queryset.filter(query)

        return queryset

    def get_search_form(self):

        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):

        if self.form.is_valid():
            return self.form.cleaned_data['search']

        return None




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








