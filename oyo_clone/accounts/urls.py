from django.urls import path
from .views import (register_view,
                    login_view,
                    otp_authentication_view,
                    verify_email_token)

urlpatterns = [
    path('register/',register_view, name = 'register'),
    path('login/', login_view, name = "login"),
    path('verify-account/<token>/', verify_email_token, name = "verify_account"),
    path('otp/', otp_authentication_view, name = "otp_auth")
]