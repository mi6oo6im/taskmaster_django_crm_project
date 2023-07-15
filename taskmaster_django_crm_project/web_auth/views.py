from taskmaster_django_crm_project.web_auth.forms import RegisterUserForm, CreateProfileForm
from django.contrib.auth import views as auth_views, login
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


class CreateProfileView(views.CreateView):
    template_name = 'web_auth/create_profile.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateProfileView(views.UpdateView):
    template_name = 'web_auth/update_profile.html'
    model = Profile
    success_url = reverse_lazy('index')
    fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number',
              'profile_picture', 'job_title', 'department']


