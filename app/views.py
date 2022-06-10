from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout


# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']
        
        if password1 != password2:
            messages.error(request, 'Check your passwords')
            return redirect('register')
        
        new_user = User.objects.create_user(username = username, email=email, password= password2)
        
        #save our user instance
        new_user.save()
    
    return render(request, 'register.html')

def user_login(request):
    return render(request, 'login.html')

def user_logout(request):
    return render(request, 'login.html')

