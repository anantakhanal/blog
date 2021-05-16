from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display= ['title' ,'date_added']




@admin.register(Company)
class AdminCompany(admin.ModelAdmin):
    pass



@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display= ['Name' ,'Email']

@admin.register(Services)
class adminServices(admin.ModelAdmin):
    list_display = ['type', 'des']
