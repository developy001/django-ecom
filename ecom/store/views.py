from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate ,login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

def home(request):
    Products = Product.objects.all()
    return render(request, 'home.html',{'Products' :Products})


def about(request):
    return render(request, 'about.html',{})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("you have Been Logged On"))
            return redirect('home')
    
        else:
            messages.success(request,("there wase an error, please try again"))
            return redirect('login')
    else:
    
        return render(request, 'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, (" you have been logged out"))
    return redirect('home')

def register_user(request):
    form = Signupform()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, (" whoops!!"))
            return redirect('home')
    else:    
        
        return render(request, 'register.html',{})
        return redirect('register')
