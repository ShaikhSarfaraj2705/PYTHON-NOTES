# =====================================================
# File: student/views.py
# =====================================================

from django.http import HttpResponse

# Home Page
def home(request):
    html = """
    <h1>Welcome to Django</h1>
    <h2>Function-Based View Example</h2>
    """
    return HttpResponse(html)

# About Page
def about(request):
    return HttpResponse("<h1>About Us</h1>")

# Contact Page
def contact(request):
    return HttpResponse("<h1>Contact Us</h1>")

# Services Page
def services(request):
    return HttpResponse("<h1>Our Services</h1>")