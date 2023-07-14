from django.http import HttpResponseRedirect

from taskmaster_django_crm_project.web_auth.forms import RegisterUserForm
from django.contrib.auth.forms import UsernameField, UserCreationForm
from django.contrib.auth import get_user_model, views as auth_views, login
from django.contrib.auth import login as auth_login
from django.views import generic as views
from django.urls import reverse_lazy


class RegisterUserView(views.CreateView):
    template_name = 'web_auth/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response


class LoginUserView(auth_views.LoginView):
    template_name = 'web_auth/login.html'


class LogoutUserView(auth_views.LogoutView):
    template_name = 'web_auth/logout.html'


class CreateProfileView(views.CreateView):
    pass


class UpdateProfileView(views.CreateView):
    pass


class DeleteProfileView(views.CreateView):
    pass
