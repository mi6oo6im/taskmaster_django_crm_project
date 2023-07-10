from django.urls import path, include
from .views import DisplayHomepage, DisplayDashboard, CreateCustomer, EditCustomer, DeleteCustomer, CreateTask,\
    EditTask, DeleteTask, DisplayAllTasks, DisplayAllCustomers

urlpatterns = (
    path('', DisplayHomepage.as_view(), name='index'),
    path('dashboard/', DisplayDashboard.as_view(), name='my_dashboard'),
    path('customer/create/', CreateCustomer.as_view(), name='create_customer'),
    path('customer/all', DisplayAllCustomers.as_view(), name='my_customers'),
    path('customer/edit/<int:pk>/', EditCustomer.as_view(), name='edit_customer'),
    path('customer/delete/<int:pk>/', DeleteCustomer.as_view(), name='delete_customer'),
    path('task/create/', CreateTask.as_view(), name='create_task'),
    path('task/all/', DisplayAllTasks.as_view(), name='my_tasks'),
    path('task/edit/<int:pk>/', CreateTask.as_view(), name='edit_task'),
    path('task/delete/<int:pk>/', CreateTask.as_view(), name='delete_task'),
)
