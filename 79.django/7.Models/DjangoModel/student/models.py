# =====================================================
# File : student/models.py
# =====================================================

from django.db import models

class Course(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Student Model
# Parent Table
class Student(models.Model):

    # Student Name
    name = models.CharField(max_length=100)
    # Student Age
    age = models.IntegerField()
    # Student Email
    email = models.EmailField()
    # Student City
    city = models.CharField(max_length=50)

    # Many Students <-> Many Courses
    courses = models.ManyToManyField(Course)

    # Display object in Admin Panel
    def __str__(self):
        return self.name
    
# =====================================================
# ONE-TO-ONE RELATIONSHIP
# =====================================================

# Example:
# One Student has one ID Card.
# One ID Card belongs to one Student.
    
# Child Table
class IDCard(models.Model):

    # One Student -> One ID Card
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE
    )

    card_number = models.CharField(max_length=20)

    def __str__(self):
        return self.card_number
    

# =====================================================
# MANY-TO-MANY RELATIONSHIP
# =====================================================

# Example:
# One Student can enroll in many Courses.
# One Course can have many Students.
