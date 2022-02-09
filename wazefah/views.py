from django.shortcuts import render, redirect
from django.views.generic import TemplateView,View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


class BaseView(TemplateView):
    template_name = 'base.html'

class HomeView(TemplateView):
    template_name = 'HomePage.html'

class LogInView(View):
    Form = AuthenticationForm
    template1 = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.Form()
        return render(request,self.template1,{'form' : form})

    def post(self, request, *args, **kwargs):
        form = self.Form(request.POST)

        if request.user.is_authenticated:
            return redirect('/home/')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('/home/')
        else:
            messages.success(request,("The username or password in not correct please try again "))
            return redirect('/logIn/')

@login_required
def log_out(request):
    logout(request)
    return redirect('/home/')