# =====================================================
# USER REGISTRATION
# =====================================================

from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            # Save new user
            form.save()

            return redirect("login")

    else:

        form = RegisterForm()

    return render(request, "register.html", {

        "form": form

    })