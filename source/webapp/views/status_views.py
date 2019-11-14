from django.urls import reverse, reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from webapp.models import Status



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
        return reverse('webapp:status_view')


class StatusUpdateView(UpdateView):
    model = Status

    template_name = 'status/update_status.html'

    fields = ['name']

    def get_success_url(self):
        return reverse('webapp:status_view')


class StatusDeleteView(DeleteView):

    template_name = 'status/delete_status.html'

    model = Status

    context_object_name = 'status'

    success_url = reverse_lazy('webapp:status_view')
