from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import StatusForm
from webapp.models import Status
from django.views.generic import ListView
from django.urls import reverse
from django.views.generic.edit import CreateView



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

def status_update_view(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'GET':
        form = StatusForm(data={
            'name': status.name
        })
        return render(request, 'status/update_status.html', context={'form': form, 'status': status})
    elif request.method == 'POST':
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status.name = form.cleaned_data['name']
            status.save()
            return redirect('status_view')
        else:
            return render(request, 'status/update_status.html', context={'form': form, 'status': status})

def status_delete_view(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'GET':
        return render(request, 'status/delete_status.html', context={'status': status})
    elif request.method == 'POST':
        status.delete()
        return redirect('status_view')