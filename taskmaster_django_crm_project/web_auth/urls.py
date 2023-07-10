from django.urls import path
from .views import RegisterUser, LoginUser, LogoutUser, EditProfile, CreateProfile, DeleteProfile

urlpatterns = (
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('profile/create/', CreateProfile.as_view(), name='create_profile'),
    path('profile/edit/<int:pk>/', EditProfile.as_view(), name='edit_profile'),
    path('profile/delete/<int:pk>/', DeleteProfile.as_view(), name='delete_profile'),
)
