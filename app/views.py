from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .models import *
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .forms import ProfileUpdateForm

from django.db.models import Q
from django.views.generic import TemplateView, ListView

# Create your views here.

def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects':projects})


#user registration
def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']
        
        if password1 != password2:
            messages.error(request,"confirm your passwords")
            return redirect('/register')
        
        new_user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
        
        new_user.save()
        return render(request,'login.html')
    return render(request, 'register.html')


#user login function
def user_login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']  
        
        user = authenticate (request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Welcome , you are now logged in")
            return redirect ("home")
    return render(request, 'login.html')


#logout function
def user_logout(request):
    logout(request)
    return render(request, 'index.html')


def user_profile(request):
    users= User.objects.all()
    current_user = request.user
    user_projects = Project.objects.filter(user=current_user)
    print(user_projects)
    
    return render (request, 'profile.html', {'users':users, 'user_projects':user_projects})


def update_profile(request):
    
    if request.method == 'POST':
        userprofileform = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if  userprofileform.is_valid():
            userprofileform.save()
            return redirect(to='profile')
    else:
        form=ProfileUpdateForm(instance =request.user.profile)
    return render(request,'update_profile.html',{'form':form})


def user_post(request):
    if request.method=='POST':
        photo=request.FILES.get('photo')
        title=request.POST.get('title')
        description=request.POST.get('description')
        posts=Project(post_image=photo,title=title,description=description)
        
        posts.save_project_post()
        
        return redirect('home')
    return render(request, 'post.html')

def search(request):
    return render(request, 'search_results.html')


class SearchResultsView(ListView):
    model = Project
    template_name = "search_results.html"
    
    def get_queryset(self):  # new
        query = self.request.GET.get("query")
        object_list = Project.objects.filter(
            Q(title__icontains=query)
        )
        return object_list

#rating function


