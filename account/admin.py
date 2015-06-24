from django.contrib import admin

from .models import MyUser

class MyUserAdmin(admin.ModelAdmin):
	list_display = ('email','date_of_birth','is_admin','is_active','password')

admin.site.register(MyUser, MyUserAdmin)