from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
# Get the user module for auth view:
from django.views.generic import CreateView, TemplateView

UserModel = get_user_model()


class DisplayHomepageView(TemplateView):
    template_name = 'taskmaster/index.html'


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


class DisplayAllTasksView(CreateView):
    pass


class UpdateTaskView(CreateView):
    pass


class DeleteTaskView(CreateView):
    pass
