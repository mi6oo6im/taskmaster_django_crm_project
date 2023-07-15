from django.contrib.auth import forms as auth_forms, password_validation, get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _

from taskmaster_django_crm_project.web_auth.models import Profile

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['email', 'password1', 'password2']

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


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['is_deleted', 'user']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }
