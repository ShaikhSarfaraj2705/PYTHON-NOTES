from django.shortcuts import render,HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse("This is HOMEpage")
    context={
        'variable':"THIS IS SENT FROM HOME VIEWS PY FILE"
    }
    return render(request,'index.html',context)
def about(request):
    # return HttpResponse("This is ABOUTpage")
    return render(request,'about.html')
def contact(request):
    # return HttpResponse("This is CONTACTpage")
    return render(request,'contact.html')
def services(request):
    # return HttpResponse("This is SERVICESpage")
    return render(request,'services.html',)
