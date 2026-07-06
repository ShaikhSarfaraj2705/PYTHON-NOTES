from django.shortcuts import render
from .forms import StudentForm
from .models import Student


def upload_image(request):

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()

    else:
        form = StudentForm()

    return render(
        request,
        "upload.html",
        {"form": form}
    )


def profile(request):

    student = Student.objects.last()

    return render(
        request,
        "profile.html",
        {"student": student}
    )