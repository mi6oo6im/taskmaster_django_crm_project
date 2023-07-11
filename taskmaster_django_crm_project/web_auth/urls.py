from django.urls import path
from .views import RegisterUserView, LoginUserView, LogoutUserView, EditProfileView, CreateProfileView, DeleteProfileView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/create/', CreateProfileView.as_view(), name='create_profile'),
    path('profile/edit/<int:pk>/', EditProfileView.as_view(), name='edit_profile'),
    path('profile/delete/<int:pk>/', DeleteProfileView.as_view(), name='delete_profile'),
)
