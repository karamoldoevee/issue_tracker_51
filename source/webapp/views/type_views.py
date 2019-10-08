from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView

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


class type_update_view(UpdateView):
    model = Type

    template_name = 'type/update_type.html'

    fields = ['name']

    def get_success_url(self):
        return reverse('type_view')

class type_delete_view(View):
    def get(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs.get('pk'))
        return render(request, 'type/delete_type.html', context={'type': type})

    def post(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs.get('pk'))
        type.delete()
        return redirect('type_view')
