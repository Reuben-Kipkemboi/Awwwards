from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.forms import URLField


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_pic=CloudinaryField('image')
    username =models.CharField(max_length=100 , null=True)
    bio=models.TextField(null=True)
    contacts=models.CharField(max_length=300)
    
    def __str__(self):
        return self.user.username
    
    
    def save_profile(self):
        self.save()
        
        
    def delete_profile(self):
        self.delete()
        
    def update_profile(self):
        self.update()
    
class Project(models.Model):
    title=models.CharField(max_length=100, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True )
    post_image=CloudinaryField('post_image')
    description=models.TextField(null=False)
    url = models.URLField(null=True)
    company = models.CharField(max_length=200, blank=True)
    languages = models.CharField(max_length=100, blank=True)
    posted_at=models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, null = True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def save_project_post(self):
        self.save()
        
    def delete_project_post(self):
        self.delete()
        
    def update_project_post(self):
        self.update()
        
class Rating(models.Model):
    project_name = models.CharField(max_length=100,null=True, blank=True)
    comment = models.CharField(max_length=1000, null=True)
    design = models.IntegerField(null=True,default=0)
    usability = models.IntegerField(null=True,default=0)
    content = models.IntegerField(null=True,default=0)
    creativity = models.IntegerField(null=True,default=0)
    total =  models.IntegerField(null=True,default=0)
    average=models.FloatField(max_length=10,null=True)
    rator = models.ForeignKey(User,null = True, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='rating',null=True, on_delete=models.CASCADE)
    rating_date = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def __str__(self):
        return self.comment
    
    def save_rating(self):
        self.save()
        
    def delete_rating(self):
        self.save()
        
    def update_rating(self):
        self.update()






