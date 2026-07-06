from django.urls import path
from . import views

urlpatterns = [

    path("", views.upload_image, name="upload"),

    path("profile/", views.profile, name="profile"),

]