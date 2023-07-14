from django.urls import path, include
from .views import DisplayHomepageView, DisplayDashboardView, CreateCustomerView, UpdateCustomerView, DeleteCustomerView, CreateTaskView,\
    UpdateTaskView, DeleteTaskView, DisplayAllTasksView, DisplayAllCustomersView

urlpatterns = (
    path('', DisplayHomepageView.as_view(), name='index'),
    path('dashboard/', DisplayDashboardView.as_view(), name='my_dashboard'),
    path('customer/create/', CreateCustomerView.as_view(), name='create_customer'),
    path('customer/all', DisplayAllCustomersView.as_view(), name='my_customers'),
    path('customer/edit/<int:pk>/', UpdateCustomerView.as_view(), name='update_customer'),
    path('customer/delete/<int:pk>/', DeleteCustomerView.as_view(), name='delete_customer'),
    path('task/create/', CreateTaskView.as_view(), name='create_task'),
    path('task/all/', DisplayAllTasksView.as_view(), name='my_tasks'),
    path('task/edit/<int:pk>/', UpdateTaskView.as_view(), name='update_task'),
    path('task/delete/<int:pk>/', DeleteTaskView.as_view(), name='delete_task'),
)
