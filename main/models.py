from django.db import models
from django.contrib.auth.models import User


#User table
class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Experience = models.TextField(null=True)
    DateOfBirth = models.DateField()
    ProfilePick = models.ImageField(upload_to='profile_pics', blank=True)
    Gender = models.CharField(max_length=10, choices=[('F', 'Female'), ('M', 'Male')])

    def __str__(self):
        return self.user.username


# jobs table
class Job(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    company_name = models.TextField()
    category = models.CharField(max_length=255)
    def __str__(self):
        return self.title + " "+ self.category

class AppliedJob(models.Model):
    user = models.ForeignKey(UserInformation,on_delete=models.CASCADE,null=True)
    job = models.ForeignKey(Job,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.user) +"-"+ str(self.job)