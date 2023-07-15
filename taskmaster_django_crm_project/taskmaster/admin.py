from django.contrib import admin
from .models import Organization, Customer, Contact, Task, Offer, Contract


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'email', 'company']
    search_fields = ["name", 'company', 'email']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'company']
    search_fields = ["title", 'company']


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'company', 'potential_annual_value', 'valid_until']
    ordering = ['valid_until']
    search_fields = ["title", 'company']


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'company', 'is_active', 'annual_value', 'end_date']
    search_fields = ["title", 'company']
