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
