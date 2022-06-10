from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def user_login(request):
    return render(request, 'login.html')

def user_logout(request):
    return render(request, 'login.html')

