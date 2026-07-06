# =====================================================
# File : student/admin.py
# =====================================================

from django.contrib import admin
from .models import Student




@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    # Display columns in the admin list page
    list_display = (
        "id",
        "name",
        "age",
        "email",
        "city",
        "active",
    )

    # Enable search box
    search_fields = (
        "name",
        "email",
    )

    # Add filter sidebar
    list_filter = (
        "city",
        "active",
    )

    # Sort records by name
    ordering = (
        "name",
    )

     # Arrange fields while adding/editing records
    # fields = (
    #     "name",
    #     "age",
    #     "email",
    #     "city",
    #     "active",
    # )

    fieldsets = (

        ("Personal Information", {

            "fields": (
                "name",
                "age",
            )
        }),

        ("Contact Information", {

            "fields": (
                "email",
                "city",
            )
        }),

        ("Status", {

            "fields": (
                "active",
            )
        }),

    )

    # User cannot edit these fields
    readonly_fields = (
        "id",
    )

    actions = [
        "make_active",
    ]
