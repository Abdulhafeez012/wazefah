from django.shortcuts import (
    render,
    redirect,
)
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth import (
    login,
    logout,
    authenticate,
)
from . import forms
from .forms import (
    UserForm,
    UserFormUpdate,
    UserProfileForm
)
from .models import (
    AppliedJob,
    Job,
    UserInformation,
    Experience,
    Company,
)
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .filter import JobFilter
from django.urls import reverse_lazy
from django import forms


class BaseView(TemplateView):
    template_name = 'base.html'


class HomeView(ListView):
    template_name = 'home_page.html'
    model = Company
    context_object_name = "companies"


class SignUp(TemplateView):
    template_name = 'sign_up.html'
    user_form = UserForm
    profile_form = UserProfileForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = self.user_form
        return context

    def post(self, request, *args, **kwargs):
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = User.objects.create_user(
                username=user_form.cleaned_data.get('username'),
                password=user_form.cleaned_data.get('password2')
            )
            UserInformation.objects.create(user=user)

            print(user)

            if user.is_authenticated and user.is_active:
                login(request, user)
                return redirect('main:user_home')
        else:
            print(user_form.errors)

        return render(request, self.template_name, {'user_form': user_form})


class LogInView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('main:user_home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


@login_required
def log_out(request):
    logout(request)
    return redirect('main:home')


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile_page.html'
    user_form = UserFormUpdate
    profile_form = UserProfileForm

    def get_context_data(self, **kwargs):
        experiences = Experience.objects.filter(
            user_id=self.request.user.id).values()
        applied_list = AppliedJob.objects.filter(
            user=self.request.user.id)
        context = super().get_context_data(**kwargs)
        context['user_form'] = self.user_form
        context['profile_form'] = self.profile_form
        context['experiences_list'] = experiences
        context['applied_list'] = applied_list
        return context

    def post(self, request, *args, **kwargs):
        user_form = UserFormUpdate(request.POST, instance=request.user)
        profile_form = UserProfileForm(
            request.POST, request.FILES, instance=request.user.userinformation)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request, 'Your profile has been updated successfully!')
            return redirect('main:user_home')
        else:
            messages.error(request, 'Incomplete info!')

        return redirect('main:profile')


# The LoginRequiredMixin it's the same of login_required but for classes
class SuggestionJobView(LoginRequiredMixin, TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        applied = AppliedJob.objects.filter(
            user=self.request.user.id).values_list('job', flat=True)
        applied_list = list(applied)

        job_list = [
            Job.objects.filter(category='IT').first(),
            Job.objects.filter(category='Retail').first(),
            Job.objects.filter(category='Customer Service').first(),
            Job.objects.filter(category='Business').first(),
        ]
        context['job_list'] = job_list
        context['companies'] = Company.objects.all()
        context['applied_list'] = applied_list
        return context

    def post(self, request, *args, **kwargs):
        user_id = UserInformation.objects.get(user=request.user.id)
        job_id = Job.objects.get(id=request.POST.get('job_id'))

        if not AppliedJob.objects.filter(user=user_id, job=job_id).exists():
            applied_job = AppliedJob.objects.create(
                user=user_id,
                job=job_id,
                status='applied'
            )
            applied_job.save()
        return redirect('main:user_home')


class JobDetailView(DetailView):
    context_object_name = 'job_detail'
    model = Job
    template_name = 'main/job_detail.html'


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    fields = ['title', 'content',
              'company', 'category']

    def get_form(self, form_class=None):
        form = super(JobCreateView, self).get_form(form_class)
        return form

    def form_valid(self, form):
        user_id = UserInformation.objects.get(user=self.request.user.id)
        form.instance.user = user_id
        return super().form_valid(form)


class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = Job
    fields = ['title', 'content',
              'company', 'category']

    def get_form(self, form_class=None):
        form = super(JobUpdateView, self).get_form(form_class)
        return form

    def get_queryset(self):
        """Return Job"""
        return Job.objects.order_by('id')


class JobDeleteView(LoginRequiredMixin, DeleteView):
    model = Job
    success_url = reverse_lazy("main:user_home")


class ResultView(ListView):
    template_name = 'result_page.html'

    def get_queryset(self):
        return Job.objects.order_by('id')

    def post(self, request, *args, **kwargs):
        model = Job.objects.all()
        jobs = Job.objects.filter(
            id=request.POST.get('job_id')).values()
        applied = AppliedJob.objects.filter(user=request.user.id).values_list('job', flat=True)
        applied_list = list(applied)
        filter = JobFilter(request.POST or None, queryset=model)
        model = filter.qs
        if request.POST.get('job_id'):
            user_id = UserInformation.objects.get(user=request.user.id)
            job_id = Job.objects.get(id=request.POST.get('job_id'))

            if not AppliedJob.objects.filter(user=user_id, job=job_id).exists():
                applied_job = AppliedJob.objects.create(
                    user=user_id,
                    job=job_id
                )
                applied_job.save()

        context = {
            'filter': filter,
            'job_model': model,
            'applied': applied_list,
            'jobs_list': jobs
        }

        return render(request, self.template_name, context)


class ExperienceListView(ListView):
    context_object_name = "experience"

    def get_queryset(self):
        """Return Experiences"""
        return Experience.objects.order_by('id')


class ExperienceDetailView(DetailView):
    context_object_name = 'experience_detail'
    model = Experience
    template_name = 'main/experience_detail.html'


class ExperienceCreateView(LoginRequiredMixin, CreateView):
    model = Experience
    fields = ['position', 'start_date',
              'end_date', 'company_name', 'description']

    def get_form(self, form_class=None):
        form = super(ExperienceCreateView, self).get_form(form_class)
        form.fields['start_date'].widget = forms.DateInput(attrs={'type': 'date'})
        form.fields['end_date'].widget = forms.DateInput(attrs={'type': 'date'})
        return form

    def form_valid(self, form):
        user_id = UserInformation.objects.get(user=self.request.user.id)
        form.instance.user = user_id
        return super().form_valid(form)


class ExperienceUpdateView(LoginRequiredMixin, UpdateView):
    models = Experience
    fields = ['position', 'start_date',
              'end_date', 'company_name', 'description']

    def get_form(self, form_class=None):
        form = super(ExperienceUpdateView, self).get_form(form_class)
        form.fields['start_date'].widget = forms.DateInput(attrs={'type': 'date'})
        form.fields['end_date'].widget = forms.DateInput(attrs={'type': 'date'})
        return form

    def get_queryset(self):
        """Return Experience"""
        return Experience.objects.order_by('id')


class ExperienceDeleteView(LoginRequiredMixin, DeleteView):
    model = Experience
    success_url = reverse_lazy("main:profile")


class SuccessView(TemplateView):
    template_name = 'success_page.html'
