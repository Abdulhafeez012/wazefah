from django.shortcuts import render
from django.views.generic import TemplateView,View
# Create your views here.

class BaseView(TemplateView):
    template_name = 'base.html'