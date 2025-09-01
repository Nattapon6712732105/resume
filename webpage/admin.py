from django.contrib import admin
from . import models

@admin.register(models.Students)
class studentsAdmin(admin.ModelAdmin):
    list_display = ('stid', 'name_prefix', 'first_name', 'last_name', 'age')
    search_fields = ('first_name', 'last_name')
    
