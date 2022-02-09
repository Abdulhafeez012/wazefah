from django.contrib import admin

from .models import Job


# Register your models here.
admin.site.register(Job)

from .models import UserInformation
# Register your models here.
admin.site.register(UserInformation)

