from django.contrib import admin

# Register your models here
from .models import User_info

class User_Admin (admin.ModelAdmin):
    list =('id','name','age','gender','weight','height','created_on','username','password')


admin.site.register(User_info, User_Admin)