from django import forms
from django.http import HttpResponseRedirect

from taskmaster_django_crm_project.web_auth.forms import RegisterUserForm
from django.contrib.auth.forms import UsernameField, UserCreationForm
from django.contrib.auth import get_user_model, views as auth_views, login
from django.contrib.auth import login as auth_login
from django.views import generic as views
from django.urls import reverse_lazy

from taskmaster_django_crm_project.web_auth.models import Profile


class RegisterUserView(views.CreateView):
    template_name = 'web_auth/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('create_profile')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response


class LoginUserView(auth_views.LoginView):
    template_name = 'web_auth/login.html'


class LogoutUserView(auth_views.LogoutView):
    template_name = 'web_auth/logout.html'


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['is_deleted', 'user']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }


class CreateProfileView(views.CreateView):
    template_name = 'web_auth/create_profile.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateProfileView(views.CreateView):
    pass


class DeleteProfileView(views.CreateView):
    pass
