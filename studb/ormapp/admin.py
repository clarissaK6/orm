from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa')
    search_fields = ('first_name', 'last_name', 'email', 'field_of_study')
    list_filter = ('field_of_study',)

