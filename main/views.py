from django.shortcuts import render, redirect
from .forms import UserForm
from django.views.generic import TemplateView, View, CreateView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Job

class BaseView(TemplateView):
    template_name = 'base.html'


class HomeView(TemplateView):
    template_name = 'HomePage.html'


class SignUp(TemplateView):
    template_name = 'SignUp.html'
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
                return redirect('/home/')

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
            return redirect('/home/')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            messages.success(request, ("The username or password in not correct please try again "))
            return redirect('/logIn/')


@login_required
def log_out(request):
    logout(request)
    return redirect('/home/')


# the job table
class JobView(CreateView):
    job_one = Job(title='Developer', content='front end and back end developer', company_name='Sitech', category='IT')
    job_one.save()

    job_two = Job(title='Nutritionist', content='medicals diets ', company_name='Istishari hospital', category='Medical')
    job_two.save()

    job_three = Job(title='Archetict', content='illestrate the models ', company_name='Iemar', category='Engeneering')
    job_three.save()

    job_four = Job(title='Animator', content='motion graphic ', company_name='PwC', category='Design')
    job_four.save()

    job_five = Job(title='Data Scienticst', content='analyze data', company_name='Amazon', category='IT')
    job_five.save()

    job_six = Job(title='Doctor', content='sell and describe madicine', company_name='pharmacy one', category='Medical')
    job_six.save()

    job_seven = Job(title='civil engeneer', content='supervise and manage the sites', company_name='Omran', category='Engeneering')
    job_seven.save()

    job_eight = Job(title='Graphic designer', content='design and do logos', company_name='Pixitoon', category='Design')
    job_eight.save()