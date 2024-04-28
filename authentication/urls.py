from django.urls import path
from authentication.views import (
    RegistrationView,
    ActivateView,
    ActivationConfirm,
    GetCSRFToken,
    CheckAuthenticatedView,
    LoginView,
    LogoutView,
    UserDetailView,
    ChangePasswordView,
    DeleteAccountView, 
    ResetPasswordEmailView, 
    ResetPasswordView, 
    ResetPasswordConfirmView
)


urlpatterns = [
    path('csrf_cookie/', GetCSRFToken.as_view(), name='csrf_cookie'),
    path('checkauth/', CheckAuthenticatedView.as_view(), name='check_auth'),
    path('registration/', RegistrationView.as_view(), name='register'),
    path('activate/<str:uid>/<str:token>/', ActivateView.as_view(), name='activate'),
    path('activate/', ActivationConfirm.as_view(), name='activation_confirm'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserDetailView.as_view(), name='user_detail'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('delete/', DeleteAccountView.as_view(), name='user_delete'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset_password/', ResetPasswordEmailView.as_view(), name='reset_password_email'),
    path('reset_password/<str:uid>/<str:token>/', ResetPasswordView.as_view(), name='reset_password'),
    path('reset_password_confirm/', ResetPasswordConfirmView.as_view(), name='reset_password_confirm'),
]