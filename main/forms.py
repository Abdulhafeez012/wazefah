from django import forms
from django.contrib.auth.models import User
from .models import UserInformation, Job
from django.contrib.auth.forms import UserCreationForm


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
        fields = ('ProfilePic', 'CareerPath', 'Bio', 'Experience', 'Gender')
