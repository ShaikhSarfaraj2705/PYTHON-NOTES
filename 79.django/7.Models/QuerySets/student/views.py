from django.http import HttpResponse
from .models import Student

# =====================================================
# RETRIEVE ALL RECORDS
# URL: /all/
# =====================================================
def all_students(request):

    students = Student.objects.all()

    data = ""

    for student in students:
        data += f"{student.name} - {student.age} - {student.city}<br>"

    return HttpResponse(data)


# =====================================================
# FILTER RECORDS
# URL: /filter/
# =====================================================
def filter_students(request):

    students = Student.objects.filter(city="Pune")

    data = ""

    for student in students:
        data += f"{student.name} - {student.city}<br>"

    return HttpResponse(data)


# =====================================================
# EXCLUDE RECORDS
# URL: /exclude/
# =====================================================
def exclude_students(request):

    students = Student.objects.exclude(city="Pune")

    data = ""

    for student in students:
        data += f"{student.name} - {student.city}<br>"

    return HttpResponse(data)


# =====================================================
# GET SINGLE RECORD
# URL: /get/
# =====================================================
def get_student(request):

    student = Student.objects.get(id=1)

    return HttpResponse(f"{student.name} - {student.city}")


# =====================================================
# FIRST RECORD
# URL: /first/
# =====================================================
def first_student(request):

    student = Student.objects.first()

    return HttpResponse(f"{student.name} - {student.city}")


# =====================================================
# LAST RECORD
# URL: /last/
# =====================================================
def last_student(request):

    student = Student.objects.last()

    return HttpResponse(f"{student.name} - {student.city}")


# =====================================================
# ORDER BY ASCENDING
# URL: /ascending/
# =====================================================
def ascending_students(request):

    students = Student.objects.order_by("name")

    data = ""

    for student in students:
        data += f"{student.name}<br>"

    return HttpResponse(data)


# =====================================================
# ORDER BY DESCENDING
# URL: /descending/
# =====================================================
def descending_students(request):

    students = Student.objects.order_by("-name")

    data = ""

    for student in students:
        data += f"{student.name}<br>"

    return HttpResponse(data)


# =====================================================
# COUNT RECORDS
# URL: /count/
# =====================================================
def count_students(request):

    total = Student.objects.count()

    return HttpResponse(f"Total Students : {total}")


# =====================================================
# CHECK RECORD EXISTS
# URL: /exists/
# =====================================================
def student_exists(request):

    exists = Student.objects.filter(city="Pune").exists()

    return HttpResponse(f"Exists : {exists}")


# =====================================================
# VALUES
# URL: /values/
# =====================================================
def values_students(request):

    students = Student.objects.values()

    data = ""

    for student in students:
        data += f"{student}<br>"

    return HttpResponse(data)


# =====================================================
# VALUES LIST
# URL: /valueslist/
# =====================================================
def values_list_students(request):

    students = Student.objects.values_list("name", "city")

    data = ""

    for student in students:
        data += f"{student}<br>"

    return HttpResponse(data)


# =====================================================
# FILTER MULTIPLE CONDITIONS
# URL: /multiple/
# =====================================================
def multiple_filter(request):

    students = Student.objects.filter(
        city="Pune",
        age=22
    )

    data = ""

    for student in students:
        data += f"{student.name}<br>"

    return HttpResponse(data)


# =====================================================
# LOOKUP EXAMPLES
# URL: /lookup/
# =====================================================
def lookup_examples(request):

    students = Student.objects.filter(name__startswith="R")

    data = ""

    for student in students:
        data += f"{student.name}<br>"

    return HttpResponse(data)