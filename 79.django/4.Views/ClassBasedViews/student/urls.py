# =====================================================
# File: student/urls.py
# =====================================================

from django.urls import path
from .views import HomeView, AboutView, ContactView

urlpatterns = [

    # Home Page
    path('', HomeView.as_view()),

    # About Page
    path('about/', AboutView.as_view()),

    # Contact Page
    path('contact/', ContactView.as_view()),
]