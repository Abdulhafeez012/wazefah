from datetime import datetime
from django import forms
from django_filters import FilterSet
from django_filters import (
    CharFilter,
    DateFilter,
    ModelChoiceFilter,
)
from .models import Job, Company


class JobFilter(FilterSet):
    title = CharFilter(label='Job Title')
    company = ModelChoiceFilter(queryset=Company.objects.all())
    category = CharFilter(label='Category')
    create_on = DateFilter(
        field_name='created_on',
        label='Created On',
        widget=forms.DateInput(
            attrs={'type': 'date', 'max': datetime.now().date()}
        )
    )

    class Meta:
        model = Job
        fields = []
