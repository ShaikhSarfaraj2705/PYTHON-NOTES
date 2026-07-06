# =====================================================
# PROJECT LEVEL URLS
# File: FirstProject/urls.py
# =====================================================

from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [

    # Admin Panel
    path('admin/', admin.site.urls),

    # Home Page
    path('', views.home),

    # About Page
    path('about/', views.about),

    # Contact Page
    path('contact/', views.contact),
]

'''
### Explanation
# path()
# Used to define a URL.

# Syntax:
path("url/", view_function)

# Example:
path("about/", views.about)

# URL:
# http://127.0.0.1:8000/about/'''