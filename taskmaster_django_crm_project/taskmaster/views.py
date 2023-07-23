from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
# Get the user module for auth view:
from django.views.generic import CreateView, TemplateView, UpdateView, ListView

from taskmaster_django_crm_project.taskmaster.models import Task

UserModel = get_user_model()


class DisplayHomepageView(TemplateView):
    template_name = 'taskmaster/index.html'


class CreateOrganisationView(CreateView):
    pass


class UpdateOrganisationView(UpdateView):
    pass


class DisplayDashboardView(CreateView):
    pass


class CreateCustomerView(CreateView):
    pass


class DisplayAllCustomersView(CreateView):
    pass


class UpdateCustomerView(CreateView):
    pass


class DeleteCustomerView(CreateView):
    pass


class CreateTaskView(CreateView):
    pass


class DisplayAllTasksView(ListView):
    model = Task
    template_name = 'taskmaster/my_tasks.html'

class UpdateTaskView(CreateView):
    pass


class DeleteTaskView(CreateView):
    pass

# create test view

