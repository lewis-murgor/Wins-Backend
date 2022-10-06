from django.urls import path
from . import views

urlpatterns = [
    path('accounts/register/', views.RegistrationView.as_view(), name='register'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view()),
    path('wins/', views.WinView.as_view()),
    path('comments/', views.CommentView.as_view()),
    path('profile_id/<int:id>/', views.SingleProfile.as_view()),
]