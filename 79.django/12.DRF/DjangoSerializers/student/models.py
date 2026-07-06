# =====================================================
# STUDENT MODEL
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

    # Display object name
    def __str__(self):
        return self.name