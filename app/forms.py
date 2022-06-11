from django import forms
from django.contrib.auth.models import User
from . models import *

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
