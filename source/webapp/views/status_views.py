from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from webapp.forms import StatusForm
from webapp.models import Status
from django.core.paginator import Paginator




class StatusView(ListView):
    template_name = 'status/status_view.html'

    context_object_name = 'statuses'

    paginate_by = 5

    paginate_orphans = 1

    def get_queryset(self):
        return Status.objects.all()

class StatusCreateView(CreateView):
    template_name = 'status/create_status.html'

    model = Status

    fields = ['name']

    def get_success_url(self):
        return reverse('status_view')


class status_update_view(UpdateView):
    model = Status

    template_name = 'status/update_status.html'

    fields = ['name']

    def get_success_url(self):
        return reverse('status_view')


class status_delete_view(DeleteView):

    template_name = 'status/delete_status.html'

    model = Status

    context_object_name = 'status'

    success_url = reverse_lazy('status_view')
