from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from .models import (HotelUser)
from .utils import generateRandomToken,sendEmailToken
from django.http import HttpResponse
# Create your views here.
def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_no')
        
        hotel_user = HotelUser.objects.filter( Q(email = email) | Q(phone_number = phone_number))

        if hotel_user.exists():
            messages.error(request, "Account exists with Email or Phone Number")
            return redirect("register")
        
        hotel_user = HotelUser.objects.create(
            username = phone_number,
            first_name = first_name,
            last_name = last_name,
            email = email,
            phone_number = phone_number,
            email_token = generateRandomToken()
        )
        hotel_user.set_password(password)
        hotel_user.save()
        sendEmailToken(email, hotel_user.email_token)
        messages.success(request,"User created Successfully")
        return redirect("register")
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


def verify_email_token(request, token):
    try:
        hotel_user = HotelUser.objects.get(email_token = token)
        hotel_user.is_verified = True
        hotel_user.save()
        messages.success(request, "Email is Verified")
        return redirect("login")
    except Exception as e:
        return HttpResponse("Invalid Token")