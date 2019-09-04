
from django.contrib.auth.admin import UserAdmin
from .models import Timestamp,User,Work,Subject,Userprofile

from django.contrib import admin


# admin.site.register(Timestamp)
# sadmin.site.register(User)

admin.site.register(Work)
admin.site.register(Userprofile)
admin.site.register(Subject)
# admin.site.register(text_append)

