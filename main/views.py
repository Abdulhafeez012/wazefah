from django.shortcuts import (
    render, 
    redirect,
)
from django.views.generic import (
    TemplateView,
    ListView,
)
from django.contrib.auth import (
    login, 
    logout, 
    authenticate,
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .filter import JobFilter
from .models import (
    AppliedJob, 
    Job, 
    UserInformation,
)
from .forms import UserForm


class BaseView(TemplateView):
    template_name = 'base.html'


class HomeView(TemplateView):
    template_name = 'home_page.html'
    

class SignUp(TemplateView):
    template_name = 'sign_up.html'
    user_form = UserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = self.user_form
        return context

    def post(self, request, *args, **kwargs):
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            if user:
                login(request, user)
                return redirect('main:user_home')

        return render(request, self.template_name, {'user_form': user_form})


class LogInView(TemplateView):
    Form = AuthenticationForm
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.Form
        return context

    def post(self, request, *args, **kwargs):
        #use request.POST instead form.cleaned_date becuase the AuthenticationForm is class of Form not model form 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('main:user_home')
        
        messages.success(request, ("The username or password in not correct please try again "))
        return redirect('main:login')


@login_required
def log_out(request):
    logout(request)
    return redirect('main:home')

# The LoginRequiredMixin it's the same of login_required but for classes
class SuggestionJobView(LoginRequiredMixin,TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job_list = [
            Job.objects.filter(category='IT').first(),
            Job.objects.filter(category="Medical").first(),
            Job.objects.filter(category='Engineering').first(),
            Job.objects.filter(category='Design').first(),
        ]
        context['job_list'] = job_list
        return context
    
    def post(self,request,*args,**kwargs):
        user_id= UserInformation.objects.get(user=request.user.id)
        job_id = Job.objects.get(id=request.POST.get('job_id'))
        applied_job = AppliedJob.objects.create(
            user=user_id,
            job=job_id
            )
        applied_job.save()
        return redirect('main:user_home')

class ResultView(ListView):
    template_name = 'result_page.html'

    def get(self,request,*args,**kwargs):
        filter = JobFilter()
        context = {
            'filter' : filter,
        }
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        model = Job.objects.all().values()
        filter = JobFilter(request.POST, queryset=model)
        model = filter.qs
        context = {
            'filter' : filter,
            'job_model' : model,
        }
        if request.POST.get('job_id'):
            user_id= UserInformation.objects.get(user=request.user.id)
            job_id = Job.objects.get(id=request.POST.get('job_id'))
            applied_job = AppliedJob.objects.create(
                user=user_id,
                job=job_id
                )
            applied_job.save()
        return render(request,self.template_name,context)