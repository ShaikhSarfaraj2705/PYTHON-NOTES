# =====================================================
# HANDLE FILE UPLOAD
# =====================================================

from django.shortcuts import render
from .forms import UploadForm
from django.core.files.storage import FileSystemStorage

def upload_file(request):

    if request.method == "POST":

        form = UploadForm(

            request.POST,

            request.FILES
        )

        if form.is_valid():

            uploaded_file = request.FILES["file"]
                    # Save file
            fs = FileSystemStorage()

            fs.save(uploaded_file.name, uploaded_file )


            print(uploaded_file.name)

            print(uploaded_file.size)

            print(uploaded_file.content_type)

    else:

        form = UploadForm()

    return render(request, "upload.html", {

        "form": form

    })


# =====================================================
# File : student/views.py
# =====================================================

from django.shortcuts import render
from .forms import StudentForm

def upload_image(request):

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            # Save data and image
            form.save()

            print("Image Uploaded Successfully")

    else:

        form = StudentForm()

    return render(request, "upload_image.html", {
        "form": form
    })