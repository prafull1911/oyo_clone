from django.urls import path
from .views import (register_view,
                    login_view,
                    verify_otp,
                    verify_email_token,
                    send_otp)

urlpatterns = [
    path('register/',register_view, name = 'register'),
    path('login/', login_view, name = "login"),
    path('verify-account/<token>/', verify_email_token, name = "verify_account"),
    path('verify-otp/<email>/', verify_otp, name = "verify_otp"),
    path('send-otp/<email>/',send_otp, name = 'send_otp')
]