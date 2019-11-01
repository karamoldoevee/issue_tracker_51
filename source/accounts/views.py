from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect, reverse

from accounts.models import Profile
from .forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.views.generic import DetailView, UpdateView, ListView
from django.contrib.auth.models import User


def login_view(request):

    context = {}

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        next_url = request.POST.get('next')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            if next_url:

                return redirect(next_url)

            return redirect('webapp:index')

        else:

            context['has_error'] = True

            context['next'] = next_url

            context['username'] = username

    else:

        context = {'next': request.GET.get('next')}

    return render(request, 'registration/login.html', context=context)

def logout_view(request):

    logout(request)

    return redirect('webapp:index')

def register_view(request, *args, **kwargs):

    if request.method == 'POST':

        form = UserCreationForm(data=request.POST)

        if form.is_valid():

            user = form.save()

            user.save()

            Profile.objects.create(user=user)

            login(request, user)

            return redirect('webapp:index')

    else:

        form = UserCreationForm()

    return render(request, 'user_create.html', context={'form': form})

class UserDetailView(DetailView):

    model = User

    template_name = 'user_detail.html'

    context_object_name = 'user_obj'


class UserPersonalInfoChangeView(UserPassesTestMixin, UpdateView):
    model = User

    template_name = 'user_info_change.html'

    form_class = UserChangeForm

    context_object_name = 'user_obj'

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def get_success_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(UserPassesTestMixin, UpdateView):
    model = User

    template_name = 'user_password_change.html'

    form_class = PasswordChangeForm

    context_object_name = 'user_obj'

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def get_success_url(self):
        return reverse('accounts:login')

class UserView(ListView):
    template_name = 'user_view.html'

    context_object_name = 'users'

    paginate_by = 5

    paginate_orphans = 1

    def get_queryset(self):
        return User.objects.all()



