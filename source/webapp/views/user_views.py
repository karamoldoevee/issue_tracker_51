from accounts.models import Team
from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView, DeleteView
from accounts.forms import TeamProjectForm



class UserForProjectAddView(CreateView):
    model = Team
    template_name = 'project/project_user_add.html'
    form_class = TeamProjectForm

    # def dispatch(self, request, *args, **kwargs):
    #     self.project = self.get_project()
    #     return super().dispatch(request, *args, **kwargs)
    #
    # def form_valid(self, form):
    #     self.object = self.project.team.user.create
    #     return redirect('webapp:project_view', pk=self.project.pk)
    #
    # def get_project(self):
    #     project_pk = self.kwargs.get('pk')
    #     return get_object_or_404(Project, pk=project_pk)

class UserAddView(CreateView):
    model = Team
    template_name = 'project/project_user_add.html'

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs
    #
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.project.pk})

class UserDeleteView(DeleteView):
    model = Team
    context_object_name = 'user'
    template_name = 'project/project_user_delete.html'
    success_url = reverse_lazy('webapp:project_view')