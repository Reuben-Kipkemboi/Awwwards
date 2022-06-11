from django.urls import path
from . import views 
from .views import SearchResultsView

urlpatterns = [
    path('', views.index, name='home'),
    
    path('login/', views.user_login, name='login'),
    
    path('register/', views.register, name='register'),
    
    path('logout/', views.user_logout, name='logout'),
    
    path('post/', views.user_post, name='post'),
    
    path('profile/', views.user_profile, name ='profile'),
    
    path('update_profile/', views.update_profile, name ='update'),
    
    path('search/', SearchResultsView.as_view(), name='search')
    
    
]
