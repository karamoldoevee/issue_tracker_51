from django.contrib.auth.mixins import PermissionRequiredMixin

from accounts.models import Team
from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from webapp.mixins import StatisticsMixin


class UserProjectView(StatisticsMixin, ListView):
    template_name = 'user/project_user_view.html'

    context_object_name = 'users'

    paginate_by = 5

    paginate_orphans = 1

    def get_queryset(self):
        return Team.objects.all()

class UserProjectCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'user/project_user_add.html'

    model = Team

    fields = ['user', 'project', 'work_finished']

    def get_success_url(self):
        return reverse('webapp:user_view')

    permission_required = 'accounts.add_team'

    permission_denied_message = "Доступ запрещён"


class UserProjectUpdateView(PermissionRequiredMixin, UpdateView):
    model = Team

    template_name = 'user/project_user_update.html'

    fields = ['user', 'project', 'work_finished']

    def get_success_url(self):
        return reverse('webapp:user_view')

    permission_required = 'accounts.change_team'

    permission_denied_message = "Доступ запрещён"

class UserProjectDeleteView(PermissionRequiredMixin, DeleteView):

    template_name = 'user/project_user_delete.html'

    model = Team

    context_object_name = 'user'

    success_url = reverse_lazy('webapp:user_view')

    permission_required = 'accounts.delete_team'

    permission_denied_message = "Доступ запрещён"
