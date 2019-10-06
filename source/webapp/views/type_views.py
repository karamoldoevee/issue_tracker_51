from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView

from webapp.forms import TypeForm
from webapp.models import Type
from django.core.paginator import Paginator



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


class type_update_view(View):
    def get(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs.get('pk'))
        form = TypeForm(data={
            'name': type.name
        })
        return render(request, 'type/update_type.html', context={'form': form, 'type': type})

    def post(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs.get('pk'))
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type.name = form.cleaned_data['name']
            type.save()
            return redirect('type_view')
        else:
            return render(request, 'type/update_type.html', context={'form': form, 'type': type})

def type_delete_view(request, pk):
    type = get_object_or_404(Type, pk=pk)
    if request.method == 'GET':
        return render(request, 'type/delete_type.html', context={'type': type})
    elif request.method == 'POST':
        type.delete()
        return redirect('type_view')