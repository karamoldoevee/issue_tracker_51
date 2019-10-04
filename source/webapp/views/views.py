from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from webapp.forms import IssueForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from webapp.models import Issue



class IndexView(ListView):
    template_name = 'issue/index.html'

    context_object_name = 'issues'

    paginate_by = 5

    paginate_orphans = 1

    def get_queryset(self):
        return Issue.objects.all().order_by('-created_at')

class IssueView(DetailView):

    template_name = 'issue/issue.html'

    model = Issue


class IssueCreateView(CreateView):
    template_name = 'issue/create.html'

    model = Issue

    fields = ['summary', 'description', 'status', 'type']

    def get_success_url(self):
        return reverse('index')


def issue_update_view(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == 'GET':
        form = IssueForm(data={
            'summary': issue.summary,
            'description': issue.description,
            'status': issue.status_id,
            'type': issue.type_id
        })
        return render(request, 'issue/update.html', context={'form': form, 'issue': issue})
    elif request.method == 'POST':
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue.summary = form.cleaned_data['summary']
            issue.description = form.cleaned_data['description']
            issue.status = form.cleaned_data['status']
            issue.type = form.cleaned_data['type']
            issue.save()
            return redirect('issue_view', pk=issue.pk)
        else:
            return render(request, 'issue/update.html', context={'form': form, 'issue': issue})


def issue_delete_view(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == 'GET':
        return render(request, 'issue/delete.html', context={'issue': issue})
    elif request.method == 'POST':
        issue.delete()
        return redirect('index')






