# =====================================================
# File : student/models.py
# =====================================================

from django.db import models

class Student(models.Model):

    name = models.CharField(max_length=100)

    age = models.IntegerField()

    email = models.EmailField()

    city = models.CharField(max_length=100)

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name