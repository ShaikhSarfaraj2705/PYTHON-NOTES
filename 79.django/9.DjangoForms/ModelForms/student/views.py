from django.shortcuts import render,get_object_or_404
from .models import Student
from .forms import StudentModelForm

def add_student(request):

    if request.method == "POST":

        form = StudentModelForm(request.POST)

        if form.is_valid():

            # Save data into database
            form.save()

            # Clear the form
            form = StudentModelForm()

    else:

        form = StudentModelForm()

    return render(request, "student_form.html", {
        "form": form
    })

def update_student(request, id):

    # Fetch existing student
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":

        # Bind form to existing object
        form = StudentModelForm(
            request.POST,
            instance=student
        )

        if form.is_valid():

            form.save()

    else:

        # Display existing data
        form = StudentModelForm(instance=student)

    return render(request, "student_form.html", {
        "form": form
    })