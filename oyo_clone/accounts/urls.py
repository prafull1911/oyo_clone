from django.urls import path
from .views import (register_view,
                    login_view,
                    otp_authentication_view)

urlpatterns = [
    path('register/',register_view, name = 'register'),
    path('login/', login_view, name = "login"),
    path('otp/', otp_authentication_view, name = "otp_auth")
]