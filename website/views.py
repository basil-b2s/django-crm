from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have logged in succesfully')
            return redirect('home')
        else:
            messages.success(request, 'Please Try again dude')
            return redirect('home')
    return render(request, 'home.html')

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, 'You have logged out succesfully')
    return redirect('home')


def register_user(request):
    return render(request, 'register.html')