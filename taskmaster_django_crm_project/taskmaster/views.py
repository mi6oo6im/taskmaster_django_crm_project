from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
# Get the user module for auth view:
from django.views.generic import CreateView, TemplateView, UpdateView, ListView

from taskmaster_django_crm_project.taskmaster.forms import UpdateTaskForm, CreateTaskForm
from taskmaster_django_crm_project.taskmaster.models import Task, Customer

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
    model = Task
    template_name = 'taskmaster/create_task.html'
    form_class = CreateTaskForm
    success_url = reverse_lazy('my_tasks')


class DisplayAllTasksView(ListView):
    model = Task
    template_name = 'taskmaster/my_tasks.html'

    def get_queryset(self):
        user = self.request.user

        customers = Customer.objects.filter(sales_representative__user=user)

        queryset = Task.objects.filter(company__in=customers, is_deleted=False)

        queryset = queryset.order_by('completed', 'due_date')

        return queryset


class CompleteTaskView(UpdateView):
    model = Task
    fields = []
    template_name = 'taskmaster/complete_task.html'
    success_url = reverse_lazy('my_tasks')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.completed = True
        self.object.save()
        return super().form_valid(form)


class PendingTaskView(UpdateView):
    model = Task
    fields = []
    template_name = 'taskmaster/pending_task.html'
    success_url = reverse_lazy('my_tasks')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.completed = False
        self.object.save()
        return super().form_valid(form)


class UpdateTaskView(UpdateView):
    model = Task
    template_name = 'taskmaster/update_task.html'
    form_class = UpdateTaskForm
    success_url = reverse_lazy('my_tasks')


class DeleteTaskView(UpdateView):
    model = Task
    fields = []
    template_name = 'taskmaster/delete_task.html'
    success_url = reverse_lazy('my_tasks')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.is_deleted = True
        self.object.save()
        return super().form_valid(form)

# create test view
