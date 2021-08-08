from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

from .verifies import ActivateAccount

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="index.html"), name='logout'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    
    path ('password-reset/',
     auth_views.PasswordResetView.as_view(template_name = 'accounts/password_reset.html'),
     name = 'password_reset'),

    path ('password-reset/done/',
     auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_done.html'),
     name = 'password_reset_done'),

    path ('password-reset-confirm/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name = 'accounts/password_reset_confirm.html'),
     name = 'password_reset_confirm'),

    path ('password-reset-complete/',
     auth_views.PasswordResetCompleteView.as_view(template_name = 'accounts/password_reset_complete.html'),
     name = 'password_reset_complete'),

]
