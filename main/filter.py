from datetime import datetime
from django import forms
from django_filters import FilterSet
from django_filters import (
    CharFilter, 
    DateFilter,
)
from .models import Job

class JobFilter(FilterSet):
    title = CharFilter(label='Job Title')
    company_name = CharFilter(label='Company Name')
    category = CharFilter(label='Category')
    create_on = DateFilter(
        field_name='created_on',
        label='Created On',
        widget=forms.DateInput(
            attrs={'type' : 'date','max' : datetime.now().date()}
            )
        )
    class Meta:
        model = Job
        fields = []
        
        
    