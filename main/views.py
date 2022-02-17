from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileForm, UserFormUpdate
from . import models
from django.views.generic import (TemplateView, View, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Job
from django.urls import reverse_lazy


class BaseView(TemplateView):
    template_name = 'base.html'


class HomeView(BaseView, TemplateView):
    template_name = 'home-page.html'


class SignUp(TemplateView):
    template_name = 'sign-up.html'
    user_form = UserForm
    profile_form = UserProfileForm

    def get(self, request, *args, **kwargs):
        uform = self.user_form
        return render(request, self.template_name, {'user_form': uform})

    def post(self, request, *args, **kwargs):
        registered = False
        user_form = UserForm(data=request.POST)
        profile_form = self.profile_form(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

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


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile-page.html'
    user_form = UserFormUpdate
    profile_form = UserProfileForm

    def get(self, request, *args, **kwargs):
        exp = models.Experience.objects.all()
        user_form = self.user_form
        profile_form = self.profile_form

        return render(request, self.template_name,
                      {'u_form': user_form, 'p_form': profile_form, 'exp': exp})

    def exp_location(request):
        return render(request, template_name='main/experience_list.html', )

    def post(self, request, *args, **kwargs):
        user_form = UserFormUpdate(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userinformation)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated succesfully!')
            return redirect('/home/SugJob/')
        else:
            messages.error(request, 'Incomplete info!')

        return render(request, self.template_name, {'u_form': user_form, 'p_form': profile_form})


@login_required
def log_out(request):
    logout(request)
    return redirect('/home/')


# The LoginRequiredMixin it's the same of login_required but for classes
class SuggestionJobView(LoginRequiredMixin, TemplateView):
    template_name = 'home-page.html'
    List1 = Job.objects.filter(category='IT').first()
    List2 = Job.objects.filter(category="Medical").first()
    List3 = Job.objects.filter(category='Engineering').first()
    List4 = Job.objects.filter(category='Design').first()

    def get(self, request, *args, **kwargs):
        model = self.List1
        model2 = self.List2
        model3 = self.List3
        model4 = self.List4
        context = {
            'model': model,
            'model2': model2,
            'model3': model3,
            'model4': model4,
        }
        return render(request, self.template_name, context)


class ResultView(ListView):
    template = 'result-page.html'
    Model = Job

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/home/SugJob')
        return redirect('/home/')

    def post(self, request, *args, **kwargs):
        SearchBar = request.POST['SearchBar']
        jobs = self.Model.objects.filter(title=SearchBar)
        context = {
            'SearchBar': SearchBar,
            'jobs': jobs,
        }
        return render(request, self.template, context)


class ExperienceListView(ListView):
    context_object_name = "experience"

    def get_queryset(self):
        """Return Experiences"""
        return models.Experience.objects.order_by('id')


class ExperienceDetailView(DetailView):
    context_object_name = 'exp_detail'
    model = models.Experience
    template_name = 'main/experience_detail.html'


class ExperienceCreateView(CreateView):
    model = models.Experience
    fields = '__all__'


class ExperienceUpdateView(UpdateView):
    models = models.Experience
    fields = '__all__'

    def get_queryset(self):
        """Return Experience"""
        return models.Experience.objects.order_by('id')


class ExperienceDeleteView(DeleteView):
    model = models.Experience
    success_url = reverse_lazy("main:detail")
