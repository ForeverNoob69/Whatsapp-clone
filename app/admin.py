from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Message)
admin.site.register(Room)
admin.site.register(Profile)

class AccountInline(admin.StackedInline):
    model= Profile
    can_delete = False

class customizedUser(UserAdmin):
    inlines = (AccountInline,)

admin.site.unregister(User)
admin.site.register(User, customizedUser)