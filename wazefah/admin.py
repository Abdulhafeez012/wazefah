from django.contrib import admin
from .models import UserInformation
from .models import Job

admin.site.register(Job)
admin.site.register(UserInformation)

