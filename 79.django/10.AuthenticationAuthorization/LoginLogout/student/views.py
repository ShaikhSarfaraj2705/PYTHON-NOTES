# =====================================================
# USER LOGIN
# =====================================================

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import RegisterForm


# -----------------------------------------------------
# Register
# -----------------------------------------------------
def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")

    else:

        form = RegisterForm()

    return render(request, "register.html", {
        "form": form
    })


# -----------------------------------------------------
# Login
# -----------------------------------------------------
def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("dashboard")

        else:

            return HttpResponse("Invalid Username or Password")

    return render(request, "login.html")


# -----------------------------------------------------
# Dashboard
# -----------------------------------------------------
@login_required
def dashboard(request):
    if request.user.is_authenticated:

        print("User is Logged In")

    else:

        print("User is Not Logged In")

    if request.user.is_superuser:

        print("Admin User")

    elif request.user.is_staff:

        print("Staff User")

    else:

        print("Normal User")
    return render(request, "dashboard.html")


# -----------------------------------------------------
# Logout
# -----------------------------------------------------
def user_logout(request):

    logout(request)

    return redirect("login")


def change_password(request):

    if request.method == "POST":

        form = PasswordChangeForm(

            request.user,

            request.POST

        )

        if form.is_valid():

            # Save new password
            user = form.save()

            # Keep user logged in
            update_session_auth_hash(
                request,
                user
            )

    else:

        form = PasswordChangeForm(
            request.user
        )

    return render(request, "change_password.html", {

        "form": form

    })