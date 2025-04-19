from django.shortcuts import render

# Create your views here.
def register_view(request):
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