from re import template
from django.shortcuts import render, redirect
from django.views.generic import TemplateView,View
from .models import UserInformation
# Create your views here.

class BaseView(TemplateView):
    template_name = 'base.html'

class HomeView(TemplateView):
    template_name = 'HomePage.html'
