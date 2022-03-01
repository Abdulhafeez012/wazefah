from django_filters import FilterSet
from django_filters import (
    CharFilter,
    ModelChoiceFilter,
)
from .models import Job, Company


class JobFilter(FilterSet):
    title = CharFilter(label='Job Title')
    company = ModelChoiceFilter(queryset=Company.objects.all())
    category = CharFilter(label='Category')

    class Meta:
        model = Job
        fields = []
