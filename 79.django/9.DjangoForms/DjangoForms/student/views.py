# =====================================================
# HANDLE FORM SUBMISSION
# =====================================================

from django.shortcuts import render
from .forms import StudentForm

def student_form(request):

    if request.method == "POST":

        # Fill form with submitted data
        form = StudentForm(request.POST)

        # Check validation
        if form.is_valid():

            # Access cleaned data
            name = form.cleaned_data["name"]
            age = form.cleaned_data["age"]
            email = form.cleaned_data["email"]
            city = form.cleaned_data["city"]

            print(name)
            print(age)
            print(email)
            print(city)

    else:

        # Empty form
        form = StudentForm()

    return render(request, "student_form.html", {
        "form": form
    })