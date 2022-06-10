from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    
    path('', views.user_login, name='login'),
    
    path('', views.register, name='register'),
    
    path('', views.user_logout, name='logout'),
    
]
