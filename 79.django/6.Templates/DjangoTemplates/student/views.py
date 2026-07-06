# =====================================================
# File : student/views.py
# =====================================================

from django.shortcuts import render

def home(request):

    # Render HTML page
    return render(request, "home.html")


# Passing Data to Template
def about(request):

    data = {
        "name": "Sarfaraj",
        "course": "Django",
        "age": 24,
    }

    return render(request, "about.html", data)