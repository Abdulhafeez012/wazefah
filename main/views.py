from typing import List
from unicodedata import category
from django.shortcuts import render, redirect
from .forms import UserForm
from django.views.generic import (TemplateView, View)
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Job

class BaseView(TemplateView):
    template_name = 'base.html'

class HomeView(TemplateView):
    template_name = 'home-page.html'


class SignUp(TemplateView):
    template_name = 'sign-up.html'
    user_form = UserForm

    def get(self, request, *args, **kwargs):
        uform = self.user_form
        return render(request, self.template_name, {'user_form': uform})

    def post(self, request, *args, **kwargs):
        registered = False
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            if user is not None:
                login(request, user)
                return redirect('/home/SugJob')

            registered = True
        else:
            print(user_form.errors)

        return render(request, self.template_name, {'user_form': user_form,
                                                    'registered': registered})


class LogInView(View):
    Form = AuthenticationForm
    template1 = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.Form()
        return render(request, self.template1, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.Form(request.POST)

        if request.user.is_authenticated:
            return redirect('/home/SugJob')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home/SugJob')
        else:
            messages.success(request, ("The username or password in not correct please try again "))
            return redirect('/logIn/')


@login_required
def log_out(request):
    logout(request)
    return redirect('/home/')

# The LoginRequiredMixin it's the same of login_required but for classes
class SuggestionJobView(LoginRequiredMixin,TemplateView):
    template_name = 'HomePage.html'
    List1 = Job.objects.filter(category='IT').first()
    List2 = Job.objects.filter(category="Medical").first()
    List3 = Job.objects.filter(category='Engineering').first()
    List4 = Job.objects.filter(category='Design').first()

    def get(self,request, *args, **kwargs):
        model = self.List1
        model2 = self.List2
        model3 = self.List3
        model4 = self.List4
        context = {
            'model': model,
            'model2' : model2,
            'model3' : model3,
            'model4' : model4,
            }
        return render(request,self.template_name,context)
