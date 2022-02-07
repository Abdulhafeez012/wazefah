from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInformation(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    Experiance = models.TextField(null = True)
    DateOfBirth = models.DateField()
    ProfilePick = models.ImageField(upload_to='profile_pics', blank=True)
    Gender = models.CharField(max_length=2,choices=[('M','F')])
    def __str__(self):
        return self.user.username