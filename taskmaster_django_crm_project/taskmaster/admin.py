from django.contrib import admin
from .models import Organization, Customer, Contact, Task, Offer, Contract


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'company']
    search_fields = ["name", 'email']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'due_date', 'completed']
    search_fields = ["title", 'description']
    ordering = ['due_date']


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'potential_annual_value', 'valid_until']
    ordering = ['valid_until']
    search_fields = ["title", 'description']


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'is_active', 'annual_value', 'end_date']
    search_fields = ["title", 'description']
