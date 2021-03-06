from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import SimpleSearchForm
from webapp.mixins import StatisticsMixin
from webapp.models import Issue

from django.db.models import Q
from django.utils.http import urlencode

from django.contrib.auth.mixins import PermissionRequiredMixin



class IndexView(StatisticsMixin, ListView):
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


class IssueView(StatisticsMixin, DetailView):

    template_name = 'issue/issue.html'

    model = Issue


class IssueCreateView(PermissionRequiredMixin, CreateView):
    model = Issue

    template_name = 'issue/create.html'

    fields = ['summary', 'description', 'status', 'type', 'assigned_to']

    permission_required = 'webapp.add_issue'

    permission_denied_message = "Доступ запрещён"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        return self.request.user.username

    def get_success_url(self):
        return reverse('webapp:issue_view', kwargs={'pk': self.object.pk})


class IssueUpdateView(PermissionRequiredMixin, UpdateView):
    model = Issue

    template_name = 'issue/update.html'

    fields = ['summary', 'description', 'status', 'type']

    context_object_name = 'issue'

    permission_required = 'webapp.change_issue'

    permission_denied_message = "Доступ запрещён"

    def test_func(self):
        return self.request.user.username

    def get_success_url(self):

        return reverse('webapp:issue_view', kwargs={'pk': self.object.pk})


class IssueDeleteView(PermissionRequiredMixin, DeleteView):

    template_name = 'issue/delete.html'

    model = Issue

    context_object_name = 'issue'

    success_url = reverse_lazy('webapp:index')

    permission_required = 'webapp.delete_issue'

    permission_denied_message = "Доступ запрещён"

    def test_func(self):
        return self.request.user.username








