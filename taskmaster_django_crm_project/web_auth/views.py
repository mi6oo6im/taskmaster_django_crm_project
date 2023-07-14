from taskmaster_django_crm_project.web_auth.forms import RegisterUserForm
from django.contrib.auth.forms import UsernameField, UserCreationForm
from django.contrib.auth import get_user_model, views as auth_views
from django.views import generic as views
from django.urls import reverse_lazy


# TODO change edit to update everywhere


class RegisterUserView(views.CreateView):
    template_name = 'web_auth/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')


class LoginUserView(auth_views.LoginView):
    template_name = 'web_auth/login.html'


class LogoutUserView(auth_views.LogoutView):
    template_name = 'web_auth/logout.html'


class CreateProfileView(views.CreateView):
    pass


class EditProfileView(views.CreateView):
    pass


class DeleteProfileView(views.CreateView):
    pass
