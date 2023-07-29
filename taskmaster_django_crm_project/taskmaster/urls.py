from django.urls import path
from .views import DisplayHomepageView, DisplayDashboardView, CreateCustomerView, UpdateCustomerView, \
    DeleteCustomerView, CreateTaskView, DisplayFeaturesView, DisplayTipsView, \
    UpdateTaskView, DeleteTaskView, DisplayAllTasksView, DisplayAllCustomersView, CompleteTaskView, PendingTaskView

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
)
# TODO contract, contact, offer and contract
