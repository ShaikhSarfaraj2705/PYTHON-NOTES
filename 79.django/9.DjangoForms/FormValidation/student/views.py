# =====================================================
# HANDLE FORM VALIDATION
# =====================================================
from django.http import HttpResponse
from django.shortcuts import render
from .forms import StudentForm

def student_form(request):

    if request.method == "POST":

        # Fill form using submitted data
        form = StudentForm(request.POST)

        # Validate data
        if form.is_valid():

            # Access validated data
            name = form.cleaned_data["name"]
            age = form.cleaned_data["age"]
            email = form.cleaned_data["email"]
            city = form.cleaned_data["city"]

            print(name)
            print(age)
            print(email)
            print(city)

    else:

        form = StudentForm()

    return render(request, "student_form.html", {
        "form": form
    })

def search(request):

    # Read GET parameter
    name = request.GET.get("name")

    return HttpResponse(name)
# http://127.0.0.1:8000/search/?name=Rahul

def register(request):

    if request.method == "POST":

        # Read form data
        username = request.POST.get("username")

        password = request.POST.get("password")

        print(username)

        print(password)

    return render(request, "register.html")