from django.contrib import admin
from .models import (UserInformation,
                     Job, AppliedJob,
                     Experience
                     )

admin.site.register(UserInformation)
admin.site.register(Job)
admin.site.register(AppliedJob)
admin.site.register(Experience)
