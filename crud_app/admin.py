from django.contrib import admin

from .models import *


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'short_name', 'established')
    search_fields = ('full_name', 'short_name')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'university', 'admission_year')
    search_fields = ('name',)


admin.site.register(University, UniversityAdmin)
admin.site.register(Student, StudentAdmin)
