from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from .models import (HotelUser)
from .utils import generateRandomToken,sendEmailToken,generateOtp,sendOtpToEmail
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

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
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        hotel_user = HotelUser.objects.filter(email = email)
        print(hotel_user)
        if not hotel_user.exists():
            messages.error(request, "No Account Found!!")
            return redirect("login")
        
        if not hotel_user[0].is_verified:
            messages.error(request, "The user is not verified!!!")
            return redirect("login")
        
        hotel_user = authenticate(username = hotel_user[0].username, password = password)
        
        if hotel_user:
            messages.success(request, "Login Success")
            login(request, hotel_user)
            return redirect("login")
        
        messages.error(request,"Invalid Credentials")
        return redirect("login")
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

def send_otp(request,email):
    # first I will check whether the user with email is present or not
    hotel_user = HotelUser.objects.filter(email = email)
    if not hotel_user.exists():
        messages.warning(request,"No account found")
        return redirect("login")
    
    # Now if user exists I have to send it OTP, for that I will create a function in utils.py
    otp = generateOtp()
    hotel_user.update(otp = otp) 
    hotel_user.save()
    sendOtpToEmail(email,otp)