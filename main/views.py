from multiprocessing import context
from unicodedata import category
from django.shortcuts import render, redirect
from .forms import UserForm
from django.views.generic import (TemplateView, View, ListView)
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .filter import JobFilter
from .models import Job

class BaseView(TemplateView):
    template_name = 'base.html'


class HomeView(TemplateView):
    template_name = 'home_page.html'


class SignUp(TemplateView):
    template_name = 'sign_up.html'
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


class LogInView(TemplateView):
    Form = AuthenticationForm
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.Form()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('main:suggestion_job')
        
        messages.success(request, ("The username or password in not correct please try again "))
        return redirect('main:log_in')


@login_required
def log_out(request):
    logout(request)
    return redirect('/home/')

# The LoginRequiredMixin it's the same of login_required but for classes
class SuggestionJobView(LoginRequiredMixin,TemplateView):
    template_name = 'home_page.html'

    def get(self,request, *args, **kwargs):
        job_list = [
            Job.objects.filter(category='IT').first(),
            Job.objects.filter(category="Medical").first(),
            Job.objects.filter(category='Engineering').first(),
            Job.objects.filter(category='Design').first(),
        ]
        context = {
            'job_list' : job_list,
            }
        return render(request,self.template_name,context)

class ResultView(ListView):
    result_template = 'result_page.html'
    my_filter = JobFilter

    def get(self,request,*args,**kwargs):
        job_filter = self.my_filter()
        context = {
            'job_filter' : job_filter,
        }
        return render(request,self.result_template,context)

    def post(self,request,*args,**kwargs):
        job_model = Job.objects.all()
        job_filter = self.my_filter(request.POST, queryset=job_model)
        job_model = job_filter.qs
        context = {
            'job_filter' : job_filter,
            'job_model' : job_model,
        }
        return render(request,self.result_template,context)