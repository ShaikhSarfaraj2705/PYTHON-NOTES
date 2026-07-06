from django.http import HttpResponse
from .models import Student

def create(request):

    # Create Student
    student = Student(
        name="Rahul",
        age=22,
        city="Pune"
    )
    student.save()

    return HttpResponse("Student Saved Successfully")

def read(request):

    students = Student.objects.all()
    data = ""
    for student in students:
        data += f"{student.name} - {student.city}<br>"

    return HttpResponse(data)


def update(request):

    student = Student.objects.get(id=1)
    student.city = "Mumbai"
    student.save()

    return HttpResponse("Student Updated")

def delete(request):

    student = Student.objects.get(id=1)
    student.delete()

    return HttpResponse("Student Deleted")