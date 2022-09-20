import imp
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationFrom
from django.contrib import messages

# Create your views here.

def Home(request):
    return render(request, 'home.html')

def Register(request):
    if request.method == "POST":
        request_form = UserRegistrationFrom(request.POST)
        if request_form.is_valid():
            request_form.save()
            messages.success(request,"Registration has been completed successfully")
    reg_form = UserRegistrationFrom()
    return render(request, 'register.html',{'reg_form':reg_form})