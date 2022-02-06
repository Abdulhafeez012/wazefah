from re import template
from django.shortcuts import render
from django.views.generic import TemplateView,View
# Create your views here.

class BaseView(TemplateView):
    template_name = 'base.html'

class HomeView(TemplateView):
    template_name = 'HomePage.html'