from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# sabak_42

from .models import  Student , CustomUser, UserProfile


admin.site.register(Student)
admin.site.register(UserProfile)

# sabak_43
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
   fieldsets = UserAdmin.fieldsets + (
       (None, {'fields': ('phone_number', 'tulgan_kun')}),
   )