from django.urls import path
from . import views

urlpatterns = [
    path('accounts/register/', views.RegistrationView.as_view(), name='register'),
]