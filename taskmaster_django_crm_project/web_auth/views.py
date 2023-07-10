from django.shortcuts import render

# Create your views here.
# TODO create login / logout views
from django.views.generic import CreateView


class RegisterUser(CreateView):
    pass


class LoginUser(CreateView):
    pass


class LogoutUser(CreateView):
    pass


class CreateProfile(CreateView):
    pass


class EditProfile(CreateView):
    pass


class DeleteProfile(CreateView):
    pass
