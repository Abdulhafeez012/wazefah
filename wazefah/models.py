from django.db import models

# Create your models here.


# jobs table
class Job(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    company_name = models.TextField()
    category = models.CharField(max_length=255)
