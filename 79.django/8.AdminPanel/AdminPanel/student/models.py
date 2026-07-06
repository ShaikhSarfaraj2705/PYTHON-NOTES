# =====================================================
# File : student/models.py
# =====================================================

from django.db import models

class Student(models.Model):

    # Student Name
    name = models.CharField(max_length=100)

    # Student Age
    age = models.IntegerField()

    # Student Email
    email = models.EmailField()

    # Student City
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name