from django.urls import path
from .views import RegisterView, LoginView, UpdatePasswordView, ResetPasswordView, UserProfileView, UserProfileUpdateView, UserDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', LoginView.as_view(),name='login'),
    path('update-password/', UpdatePasswordView.as_view(),name='update-password'),
    path('reset-password/', ResetPasswordView.as_view(),name='reset-password'),
    path('update-profile/', UpdatePasswordView.as_view(),name='update-profile'),
    path('profile/', UserProfileView.as_view(),name='user-profile'),

]