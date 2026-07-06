from django.db import models

class Student(models.Model):

    name = models.CharField(max_length=100)

    # Upload image into media/students/
    photo = models.ImageField(

        upload_to="students/"

    )

    def __str__(self):

        return self.name