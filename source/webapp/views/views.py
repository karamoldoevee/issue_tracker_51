from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

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


# class issue_update_view(View):
#     def get(self, request, *args, **kwargs):
#         issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
#         form = IssueForm(data={
#             'summary': issue.summary,
#             'description': issue.description,
#             'status': issue.status_id,
#             'type': issue.type_id
#         })
#         return render(request, 'issue/update.html', context={'form': form, 'issue': issue})
#
#     def post(self, request, *args, **kwargs):
#         issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
#         form = IssueForm(data=request.POST)
#         if form.is_valid():
#             issue.summary = form.cleaned_data['summary']
#             issue.description = form.cleaned_data['description']
#             issue.status = form.cleaned_data['status']
#             issue.type = form.cleaned_data['type']
#             issue.save()
#             return redirect('issue_view', pk=issue.pk)
#         else:
#             return render(request, 'issue/update.html', context={'form': form, 'issue': issue})


class issue_update_view(UpdateView):
    model = Issue

    template_name = 'issue/update.html'

    fields = ['summary', 'description', 'status', 'type']



    def get_success_url(self):
        return reverse('issue_view', kwargs={'pk': self.object.pk})


class issue_delete_view(View):
    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        return render(request, 'issue/delete.html', context={'issue': issue})

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        issue.delete()
        return redirect('index')






