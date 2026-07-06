from django.shortcuts import render
from datetime import datetime


def student(request):

    return render(request, "student.html", {
        "name": "Rahul",
        "city": "Pune",
        "age":18
    })


def home(request):

    students = ["Rahul", "Amit", "Neha", "Priya"]
    return render(request, "home.html", {
        "students": students
    })

def filter(request):
    
    return render(request,"filter.html",{"FullName": "rahul sharma",
        "city": "Pune",
        "today": datetime.now(),
        "age":18
        
        })