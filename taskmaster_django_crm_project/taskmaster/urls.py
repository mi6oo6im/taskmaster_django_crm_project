from django.urls import path
from .views import DisplayHomepageView, DisplayDashboardView, CreateCustomerView, UpdateCustomerView, \
    DeleteCustomerView, CreateTaskView, DisplayFeaturesView, DisplayTipsView, \
    UpdateTaskView, DeleteTaskView, DisplayAllTasksView, DisplayAllCustomersView, CompleteTaskView, PendingTaskView, \
    CreateContactView, UpdateContactView, DeleteContactView, DisplayContractsView, CreateContractView, \
    UpdateContractView, DeleteContractView, DisplayOffersView, CreateOfferView, UpdateOfferView, DeleteOfferView, \
    ConvertOfferToContractView

urlpatterns = (
    path('', DisplayHomepageView.as_view(), name='index'),
    path('features/', DisplayFeaturesView.as_view(), name='features'),
    path('tips/', DisplayTipsView.as_view(), name='tips'),
    path('dashboard/', DisplayDashboardView.as_view(), name='my_dashboard'),
    path('customer/create/', CreateCustomerView.as_view(), name='create_customer'),
    path('customer/all', DisplayAllCustomersView.as_view(), name='my_customers'),
    path('customer/edit/<int:pk>/', UpdateCustomerView.as_view(), name='update_customer'),
    path('customer/delete/<int:pk>/', DeleteCustomerView.as_view(), name='delete_customer'),
    path('task/create/', CreateTaskView.as_view(), name='create_task'),
    path('task/all/', DisplayAllTasksView.as_view(), name='my_tasks'),
    path('task/complete/<int:pk>/', CompleteTaskView.as_view(), name='complete_task'),
    path('task/pending/<int:pk>/', PendingTaskView.as_view(), name='pending_task'),
    path('task/update/<int:pk>/', UpdateTaskView.as_view(), name='update_task'),
    path('task/delete/<int:pk>/', DeleteTaskView.as_view(), name='delete_task'),
    path('contact/create/<int:customer_id>/', CreateContactView.as_view(), name='create_contact'),
    path('contact/update/<int:pk>/', UpdateContactView.as_view(), name='update_contact'),
    path('contact/delete/<int:pk>/', DeleteContactView.as_view(), name='delete_contact'),
    path('contract/display/<int:customer_id>/', DisplayContractsView.as_view(), name='display_contracts'),
    path('contract/create/<int:customer_id>/', CreateContractView.as_view(), name='create_contract'),
    path('contract/update/<int:pk>/', UpdateContractView.as_view(), name='update_contract'),
    path('contract/delete/<int:pk>/', DeleteContractView.as_view(), name='delete_contract'),
    path('offer/display/<int:customer_id>/', DisplayOffersView.as_view(), name='display_offers'),
    path('offer/create/<int:customer_id>/', CreateOfferView.as_view(), name='create_offer'),
    path('offer/update/<int:pk>/', UpdateOfferView.as_view(), name='update_offer'),
    path('offer/delete/<int:pk>/', DeleteOfferView.as_view(), name='delete_offer'),
    path('contract/convert/<int:customer_id>/<str:title>/<str:description>/<str:potential_annual_value>/',
         ConvertOfferToContractView.as_view(), name='convert_offer_to_contract'),
)
# TODO offer and contract
