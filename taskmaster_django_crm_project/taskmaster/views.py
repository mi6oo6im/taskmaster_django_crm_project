from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Sum, Count
from django.views.generic import CreateView, TemplateView, UpdateView, ListView
from taskmaster_django_crm_project.taskmaster.forms import UpdateTaskForm, CreateTaskForm, CreateCustomerForm, \
    UpdateCustomerForm
from taskmaster_django_crm_project.taskmaster.models import Task, Customer, Offer

UserModel = get_user_model()


class DisplayHomepageView(TemplateView):
    template_name = 'taskmaster/index.html'


class DisplayFeaturesView(TemplateView):
    template_name = 'taskmaster/key_features.html'


class DisplayTipsView(TemplateView):
    template_name = 'taskmaster/tips_and_tricks.html'


class DisplayDashboardView(ListView):
    model = Customer
    template_name = 'taskmaster/my_dashboard.html'

    def get_queryset(self):
        user = self.request.user

        queryset = Customer.objects.filter(
            sales_representative__user=user,
            is_deleted=False,
        )

        # Calculate the total ACV for all customers
        total_acv_all_customers = queryset.aggregate(total_acv=Sum('contract__annual_value'))['total_acv']

        # Calculate the total potential ACV from the Offers
        total_potential_acv_customers = queryset.aggregate(total_potential_acv=Sum('offer__potential_annual_value'))[
            'total_potential_acv']

        # Calculate the total number of customers
        total_customers = queryset.count()

        # Calculate the total number of offers
        total_offers = Offer.objects.filter(company__sales_representative__user=user).count()

        # Calculate the total number of tasks
        total_tasks = Task.objects.filter(company__sales_representative__user=user, is_deleted=False,
                                          completed=False).count()

        # Pass the calculated values to the template context
        self.total_acv_all_customers = total_acv_all_customers
        self.total_potential_acv_customers = total_potential_acv_customers
        self.total_customers = total_customers
        self.total_offers = total_offers
        self.total_tasks = total_tasks

        # Annotate the total AOV for each customer
        queryset = queryset.annotate(
            total_acv=Sum('contract__annual_value', distinct=True),
            contracts_count=Count('contract__id', distinct=True),
            potential_acv=Sum('offer__potential_annual_value', distinct=True),
            offers_count=Count('offer__id', distinct=True),
            tasks_count=Count('task__id', distinct=True),
        )

        queryset = queryset.order_by('name')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add calculated values to the context
        context['total_acv_all_customers'] = self.total_acv_all_customers
        context['total_potential_acv_customers'] = self.total_potential_acv_customers
        context['total_customers'] = self.total_customers
        context['total_offers'] = self.total_offers
        context['total_tasks'] = self.total_tasks
        return context


class CreateCustomerView(CreateView):
    model = Customer
    template_name = 'taskmaster/create_customer.html'
    form_class = CreateCustomerForm
    success_url = reverse_lazy('my_customers')


class DisplayAllCustomersView(ListView):
    model = Customer
    template_name = 'taskmaster/my_customers.html'

    def get_queryset(self):
        user = self.request.user

        queryset = Customer.objects.filter(sales_representative__user=user, is_deleted=False)

        # Annotate the total AOV for each customer
        queryset = queryset.annotate(
            total_acv=Sum('contract__annual_value', distinct=True),
            contracts_count=Count('contract__id', distinct=True),
            potential_acv=Sum('offer__potential_annual_value', distinct=True),
            offers_count=Count('offer__id', distinct=True),
        )

        queryset = queryset.order_by('name')

        return queryset


class UpdateCustomerView(UpdateView):
    model = Customer
    template_name = 'taskmaster/update_customer.html'
    form_class = UpdateCustomerForm
    success_url = reverse_lazy('my_customers')


class DeleteCustomerView(UpdateView):
    model = Customer
    fields = []
    template_name = 'taskmaster/delete_customer.html'
    success_url = reverse_lazy('my_customers')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.is_deleted = True
        self.object.save()
        return super().form_valid(form)


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

