from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import TypeForm
from webapp.models import Type
from django.views.generic import ListView
from django.urls import reverse
from django.views.generic.edit import CreateView



class TypeView(ListView):
    template_name = 'type/type_view.html'

    context_object_name = 'types'

    paginate_by = 5

    paginate_orphans = 1

    def get_queryset(self):
        return Type.objects.all()

class TypeCreateView(CreateView):
    template_name = 'type/create_type.html'

    model = Type

    fields = ['name']

    def get_success_url(self):
        return reverse('type_view')

def type_update_view(request, pk):
    type = get_object_or_404(Type, pk=pk)
    if request.method == 'GET':
        form = TypeForm(data={
            'name': type.name
        })
        return render(request, 'type/update_type.html', context={'form': form, 'type': type})
    elif request.method == 'POST':
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type.name = form.cleaned_data['name']
            type.save()
            return redirect('type_view', pk=type.pk)
        else:
            return render(request, 'type/update_type.html', context={'form': form, 'type': type})

def type_delete_view(request, pk):
    type = get_object_or_404(Type, pk=pk)
    if request.method == 'GET':
        return render(request, 'type/delete_type.html', context={'type': type})
    elif request.method == 'POST':
        type.delete()
        return redirect('type_view')