from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime


# User table
class UserInformation(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    bio = models.TextField(null=True, blank=True)
    career_path = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    date_of_birth = models.DateField(default=datetime.date.today)
    profile_pic = models.ImageField(
        default='profile_pics/default.png',
        upload_to='profile_pics'
    )
    gender = models.CharField(
        max_length=10,
        choices=[('F', 'Female'), ('M', 'Male')],
        blank=True, null=True
    )

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
        return self.title + " " + self.category


class AppliedJob(models.Model):
    user = models.ForeignKey(
        UserInformation,
        related_name='user_applied',
        on_delete=models.CASCADE,
        null=True
    )
    job = models.ForeignKey(
        Job,
        related_name='job_applied',
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return str(self.user) + "-" + str(self.job)


class Experience(models.Model):
    position = models.CharField(max_length=70)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    company_name = models.TextField()
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(
        UserInformation,
        on_delete=models.CASCADE,
        related_name='user_experience'
    )

    def get_absolute_url(self):
        return reverse('main:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.id) + "-" + self.position
