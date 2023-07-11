from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import UsernameField
from django.urls import reverse_lazy
from django.views import generic as views
from django.utils.translation import gettext_lazy as _
from django import forms

UserModel = get_user_model()


# TODO change edit to update everywhere
class RegisterUserForm(auth_forms.UserCreationForm):

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )


class RegisterUserView(views.CreateView):
    template_name = 'web_auth/register.html'
    from_class = RegisterUserForm
    model = UserModel
    fields = ['email', 'password']
    success_url = reverse_lazy('index')


class LoginUserView(views.CreateView):
    pass


class LogoutUserView(views.CreateView):
    pass


class CreateProfileView(views.CreateView):
    pass


class EditProfileView(views.CreateView):
    pass


class DeleteProfileView(views.CreateView):
    pass
