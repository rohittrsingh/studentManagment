from django.contrib import admin
from .models import School, Student


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', "name", "school"]
    list_filter = ["school"]


class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', "name"]


admin.site.register(Student, StudentAdmin)
admin.site.register(School, SchoolAdmin)
