from django import forms

from taskmaster_django_crm_project.taskmaster.models import Task, Customer, Contact, Contract


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


class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['is_deleted']


class UpdateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['is_deleted', 'company']


class CreateContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        exclude = ['is_deleted']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }