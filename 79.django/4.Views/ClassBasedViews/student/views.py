# =====================================================
# File: student/views.py
# =====================================================

from django.http import HttpResponse
from django.views import View


class HomeView(View):

    # Handles GET requests
    def get(self, request):
        return HttpResponse("<h1>Welcome to Home Page</h1>")


class AboutView(View):

    # Handles GET requests
    def get(self, request):
        return HttpResponse("<h1>About Us</h1>")


class ContactView(View):

    # Handles GET requests
    def get(self, request):
        return HttpResponse("<h1>Contact Us</h1>")