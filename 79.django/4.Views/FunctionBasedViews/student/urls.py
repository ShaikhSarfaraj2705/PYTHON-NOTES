# =====================================================
# File: student/urls.py
# =====================================================

from django.urls import path
from . import views

urlpatterns = [

    # Home Page
    path('', views.home),

    # About Page
    path('about/', views.about),

    # Contact Page
    path('contact/', views.contact),

    # Services Page
    path('services/', views.services),
]