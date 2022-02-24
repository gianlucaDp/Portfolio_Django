from django.contrib import admin
from .models import Job

@admin.register(Job)
class PetAdmin(admin.ModelAdmin):
    pass