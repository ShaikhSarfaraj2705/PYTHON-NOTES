# =====================================================
# File: student/views.py
# =====================================================

from django.shortcuts import redirect
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")

def dashboard(request):
    return HttpResponse("Dashboard")

def login(request):

    # Redirect user to dashboard page
    return redirect("/student/dashboard/")

def logout(request):

    # Redirect user to dashboard page
    return redirect("home")