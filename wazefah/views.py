from re import template
from django.shortcuts import render, redirect
from django.views.generic import TemplateView,View

from django.views.generic import CreateView
from .models import Job


from .models import UserInformation

# Create your views here.

class BaseView(TemplateView):
    template_name = 'base.html'

class HomeView(TemplateView):
    template_name = 'HomePage.html'




### the job table
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

