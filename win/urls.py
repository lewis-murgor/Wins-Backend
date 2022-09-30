from django.urls import path
from . import views

urlpatterns = [
    path('accounts/register/', views.RegistrationView.as_view(), name='register'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
]