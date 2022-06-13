from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project, Profile, Rating

class TestProfile(TestCase):
    def setUp(self):
        self.new_user=User(first_name='Reuben', last_name='Kipkemboi', username='Reuby', email='reuby@gmail.com',password='password')
        self.new_user.save()

        self.new_profile=Profile(
            user=self.new_user,profile_pic='cool_pic.jpg',username = 'Reuby',bio = 'African in New york',contacts = '0723987838 Nairobi'
        )
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))


class TestProject(TestCase):
    def setUp(self):
        self.new_project=Project(title='test', user='Reuby', post_image='test_image.jpg', description='This is a test project with test image and test credentials',url='https://test.com', company='Reuby', languages='HTML', )
        
        self.new_project.save()
        
    #instance test 
    def test_instance(self):
        self.assertTrue(isinstance(self.new_project,Project))
        
    #save test
    def test_save_method(self):
        self.new_project.save_project_post()
        user_projects = Project.objects.all()
        self.assertTrue(len(user_projects) > 0)
        
    #update test
    def test_update_project(self):
        self.new_project.save_project_post()
        user_projects = Project.objects.all()
        self.assertTrue(len(user_projects) > 0)
        
    #delete test
    def test_delete_method(self):
        self.new_project.save_project_post()
        self.new_project.delete_project_post()
        user_projects = Project.objects.all()
        self.assertTrue(len(user_projects) == 0)
        
        
        
#Rating Testcases    
class TestRating(TestCase):
    def setUp(self):
    
        rator=User.objects.create(first_name='Reuben', last_name='Kipkemboi', username='Reuby', email='reuby@gmail.com')
        
        self.new_project=Project(title='test', rator=rator, post_image='test_image.jpg', description='This is a test project with test image and test credentials',url='https://test.com', company='Reuby', languages='HTML', )
        
        
        self.rating=Rating(comment='nice project fella',design=10, usability=10, content=10, creativity=10, total=40, average=10,rator=rator, project=self.new_project )
        

