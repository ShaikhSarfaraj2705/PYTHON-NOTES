from django.contrib import admin
from .models import Student

# Register your models here.
# admin.site.register(Student)


# Header displayed on login page
admin.site.site_header = "Student Management System"

# Browser title
admin.site.site_title = "Student Admin"

# Dashboard title
admin.site.index_title = "Welcome to Django Admin Panel"


# Using the @admin.register Decorator
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # Columns displayed in Admin Panel
    list_display = ["id", "name", "age", "email", "city"]

    # Search by these fields
    search_fields = ["name", "email"]

    # Filter records
    list_filter = ["city"]

    # Default ordering
    ordering = ["name"]

    # These fields cannot be edited
    readonly_fields = ["id"]

    # # Arrange fields in the form
    # fields = ["name", "email", "age" ,"city"]


    fieldsets = (

        ("Personal Information", {

            "fields": ("name", "age")

        }),

        ("Contact Information", {

            "fields": ("email", "city")

        }),

    )