

# Create your views here.
# myapp/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("My First Django App")
