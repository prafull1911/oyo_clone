from django.shortcuts import render
from .models import (HotelUser)
# Create your views here.
def register_view(request):
    if request.method == "POST":
        first_name = request.GET.get('first_name')
        last_name = request.GET.get('last_name')
        email = request.GET.get('email')
        password = request.GET.get('password')
        phone_number = request.GET.get('phone_no')
    template_name = "accounts/registration.html"
    context = {}
    return render(request, template_name, context)


def login_view(request):
    template_name = "accounts/login.html"
    context = {}
    return render(request, template_name, context)

def otp_authentication_view(request):
    template_name = "accounts/otp_authentication.html"
    context = {}
    return render(request, template_name, context)