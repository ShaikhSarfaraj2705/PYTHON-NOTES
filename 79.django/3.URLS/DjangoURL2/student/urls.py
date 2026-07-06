# =====================================================
# APP LEVEL URLS
# File: student/urls.py
# =====================================================

from django.urls import path
from . import views

urlpatterns = [

    # URL:
    # http://127.0.0.1:8000/student/
    path('', views.home),

    # URL:
    # http://127.0.0.1:8000/student/about/
    path('about/', views.about),

    # URL:
    # http://127.0.0.1:8000/student/contact/
    path('contact/', views.contact),
]