import django_filters
from django_filters import DateFilter
from .models import Job

class JobFilter(django_filters.FilterSet):
    created_on = DateFilter(field_name='created_on')
    class Meta:
        model = Job
        fields = [
            'title',
            'company_name', 
            'category',]