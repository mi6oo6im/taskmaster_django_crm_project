from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
# Get the user module for auth view:
from django.views.generic import CreateView, TemplateView

UserModel = get_user_model()


class DisplayHomepage(TemplateView):
    template_name = 'taskmaster/index.html'


class DisplayDashboard(CreateView):
    pass


class CreateCustomer(CreateView):
    pass


class DisplayAllCustomers(CreateView):
    pass


class UpdateCustomer(CreateView):
    pass


class DeleteCustomer(CreateView):
    pass


class CreateTask(CreateView):
    pass


class DisplayAllTasks(CreateView):
    pass


class UpdateTask(CreateView):
    pass


class DeleteTask(CreateView):
    pass
