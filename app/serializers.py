from rest_framework import serializers
from .models import *

#profile
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ( 'username','profile_pic', 'bio')
        
  
#Projects      
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ( 'title','user', 'post_image', 'description', 'posted_at', 'rating')