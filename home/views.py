from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')

def login(request):
    # return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Hello, {username}, Welcome to PapuChaiWala.")
            return redirect('homes:home')

        else:
            messages.error(request, "Username and password did not match.")
            return render(request, 'login.html')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            passwd = request.POST.get('password')
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')

            # validate before creating user 
            if User.objects.filter(username=username).exists():
                messages.error.filter(request, "Username already exists")
                return render(request, 'register.html')

            if User.objects.filter(email=email).exists():
                messages.error.filter(request, "Email already exists")
                return render(request, 'register.html')

            # save in DB
            User.objects.create_user(username=username,email=email,password=passwd,first_name=fname,last_name=lname)

            messages.success(request, 'Account created successfully')
            return redirect('homes:login')
    
        except Exception:
            messages.error(request, "Something went wrong. Please try again.")
            return render(request, 'register.html')

    return render(request, 'register.html')

def logout(request):
    auth_logout(request)
    messages.info(request, "User logged out successfully")
    return redirect('homes:home')
