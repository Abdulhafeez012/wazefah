from django import forms
from django.contrib.auth.models import User
from .models import AppliedJob, UserInformation
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username', 'password1', 'password2')


class UserInformationForm(forms.ModelForm):
    class Meta():
        model = UserInformation
        fields = ('ProfilePic', 'Experience', 'Gender', 'DateOfBirth')
        

class AddJob(forms.ModelForm):
    class Meta():
        model=AppliedJob
        exclude = ['user','job']