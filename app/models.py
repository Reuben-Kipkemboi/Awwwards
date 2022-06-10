from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    profile_pic=CloudinaryField('image')
    bio=models.TextField(null=True)
    contacts=models.CharField(max_length=300)
    
    def __str__(self):
        return self.contacts
    
class Project_post(models.Model):
    title=models.CharField(max_length=100, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    post_image=CloudinaryField('image',blank=True)
    description=models.TextField(null=False)
    posted_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Rating(models.Model):
    project_name = models.CharField(max_length=100, null=True)
    design = models.IntegerField(null=True,default=0)
    usability = models.IntegerField(null=True,default=0)
    content = models.IntegerField(null=True,default=0)
    creativity = models.IntegerField(null=True,default=0)
    total =  models.IntegerField(null=True,default=0)
    average=models.FloatField(max_length=10,null=True)
    user = models.ForeignKey(User,null = True, on_delete=models.CASCADE)
    post = models.ForeignKey(Project_post, related_name='rating',null=True, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.project_name





