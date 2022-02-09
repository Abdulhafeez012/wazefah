from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User


#User Table
class UserInformation(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    Experience = models.TextField(null = True)
    DateOfBirth = models.DateField()
    ProfilePick = models.ImageField(upload_to='profile_pics', blank=True)
    Gender = models.CharField(max_length=10,choices=[('F','Female'),('M','Male')])
    def __str__(self):
        return self.user.username

# jobs table
class Job(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    company_name = models.TextField()
    category = models.CharField(max_length=255)
