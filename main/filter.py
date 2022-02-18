from ast import For
from django_filters import FilterSet
from django_filters import DateRangeFilter
from .models import Job
from django_filters.filterset import forms
from crispy_forms.helper import FormHelper

class JobFilter(FilterSet):
    created_on = DateRangeFilter(field_name='created_on')
    class Meta():
        form = forms
        model = Job
        fields = [
            'title',
            'company_name', 
            'category',
            ]

