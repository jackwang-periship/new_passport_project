from django.contrib import admin
from .models import Student


@admin.register(Student)
class studentsAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')