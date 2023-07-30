from django import forms

from taskmaster_django_crm_project.taskmaster.models import Task, Customer


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['is_deleted', 'completed']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['is_deleted', 'company', 'completed']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }


class CreateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['is_deleted']


class UpdateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['is_deleted']
