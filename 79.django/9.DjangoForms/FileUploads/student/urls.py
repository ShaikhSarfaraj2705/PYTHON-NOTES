# =====================================================
# File : student/urls.py
# =====================================================

from django.urls import path
from . import views

urlpatterns = [

    # Upload File
    path("upload/",views.upload_file,),
    path("upload-image/",views.upload_image,),
]