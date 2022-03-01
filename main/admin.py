from django.contrib import admin
from .models import (
    UserInformation,
    Job,
    AppliedJob,
    Experience,
    Company,
)

admin.site.register(UserInformation)
admin.site.register(AppliedJob)
admin.site.register(Experience)
admin.site.register(Company)
admin.site.register(Job)
