from accounts.models import Team
from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView, DeleteView, ListView, UpdateView


class UserProjectView(ListView):
    template_name = 'user/project_user_view.html'

    context_object_name = 'users'

    paginate_by = 5

    paginate_orphans = 1

    def get_queryset(self):
        return Team.objects.all()

class UserProjectCreateView(CreateView):
    template_name = 'user/project_user_add.html'

    model = Team

    fields = ['user', 'project', 'work_finished']

    def get_success_url(self):
        return reverse('webapp:user_view')


class UserProjectUpdateView(UpdateView):
    model = Team

    template_name = 'user/project_user_update.html'

    fields = ['user', 'project', 'work_finished']

    def get_success_url(self):
        return reverse('webapp:user_view')

class UserProjectDeleteView(DeleteView):

    template_name = 'user/project_user_delete.html'

    model = Team

    context_object_name = 'user'

    success_url = reverse_lazy('webapp:user_view')
