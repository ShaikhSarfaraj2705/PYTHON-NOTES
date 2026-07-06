from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Welcome to Home Page</h1>")

# Receive Integer ID
def user_detail(request, id):
    return HttpResponse(f"Student ID: {id}")

# Receive String Name
def user_profile(request, name):
    return HttpResponse(f"Welcome {name}")