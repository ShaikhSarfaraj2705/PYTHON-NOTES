# =====================================================
# COMMON MODEL FIELD TYPES
# =====================================================

from django.db import models


# =====================================================
# ONE-TO-MANY RELATIONSHIP
# =====================================================

# Example:
# One Department has many Employees.
# One Employee belongs to one Department.
class Department(models.Model):

    name = models.CharField(max_length=100,null=True,blank=True)
    

    def __str__(self):
        return self.name


class Employee(models.Model):

    # Short Text
    name = models.CharField(max_length=100)
    # Long Text
    address = models.TextField()
    # Integer Value
    age = models.IntegerField()
    # Decimal Number
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    # Email Address
    email = models.EmailField()
    # URL
    website = models.URLField()
    # Boolean (True/False)
    active = models.BooleanField(default=True)
    # Date Only
    joining_date = models.DateField()
    # Date and Time
    created_at = models.DateTimeField(auto_now_add=True)
    # Automatically Updated DateTime
    updated_at = models.DateTimeField(auto_now=True)
    # Image
    photo = models.ImageField(upload_to="photos/")
    # File Upload
    resume = models.FileField(upload_to="resume/")


    # ForeignKey creates One-to-Many relationship
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )


    def __str__(self):
        return self.name