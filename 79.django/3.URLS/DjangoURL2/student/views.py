from django.http import HttpResponse

# Create your views here.
# Home Page
def home(request):
    return HttpResponse("<h1>Welcome to Home Page</h1>")

# About Page
def about(request):
    return HttpResponse("<h1>About Us</h1>")

# Contact Page
def contact(request):
    return HttpResponse("<h1>Contact Us</h1>")