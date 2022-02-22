from django import forms
from django.contrib.auth.models import User
from .models import UserInformation, Experience
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime


class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username', 'password1', 'password2',)


class UserFormUpdate(forms.ModelForm):
    class Meta():
        model = User
        fields = ('first_name', 'last_name')


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserInformation
        fields = ('profile_pic', 'career_path', 'bio', 'gender')


class UserExpForm(forms.ModelForm):
    class Meta():
        model = Experience
        fields = '__all__'
