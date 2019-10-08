from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView

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


class status_delete_view(View):
    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs.get('pk'))
        return render(request, 'status/delete_status.html', context={'status': status})

    def post(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs.get('pk'))
        status.delete()
        return redirect('status_view')
