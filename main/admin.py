from django.contrib import admin
from .models import UserInformation, Job,AppliedJob

admin.site.register(UserInformation)
admin.site.register(Job)
admin.site.register(AppliedJob)