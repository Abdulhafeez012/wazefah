from django import forms
from django.contrib.auth.models import User
from .models import UserInformation, Experience
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Button, Submit, Div
from crispy_forms.bootstrap import FormActions


class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            Div(
                Submit(
                    'signup',
                    'Register',
                    css_class='btn btn-danger btn-block signup-btn'
                )
                , css_class='d-block'
            )
        )

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
