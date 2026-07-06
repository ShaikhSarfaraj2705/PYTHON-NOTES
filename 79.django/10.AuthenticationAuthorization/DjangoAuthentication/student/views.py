# =====================================================
# File : student/views.py
# =====================================================

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


# =====================================================
# USER LOGIN
# =====================================================

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

            # Create login session
            login(request, user)

            return redirect("dashboard")

        else:

            return render(request, "login.html", {
                "error": "Invalid Username or Password"
            })

    return render(request, "login.html")


# =====================================================
# USER LOGOUT
# =====================================================

def user_logout(request):

    # Remove Session
    logout(request)

    return redirect("login")


# =====================================================
# DASHBOARD
# =====================================================

@login_required
def dashboard(request):

    if request.user.has_perm("student.add_student"):

        print("Can Add Student")

    else:

        print("Permission Denied")

    if request.user.is_authenticated:

        print("User Logged In")

    else:

        print("User Not Logged In")

    return render(request, "dashboard.html")


# =====================================================
# PROFILE
# =====================================================

@login_required
def profile(request):
    if request.user.has_perms(

    [

        "student.add_student",

        "student.change_student"

    ]

    ):
        print("Access Granted")

    return render(request, "profile.html")


@permission_required(
    "student.delete_student",
    raise_exception=True
)

def delete_student(request):
    pass



def admin_panel(request):

    if request.user.is_superuser:
        print("Administrator")

def admin_page(request):

    if request.user.is_staff:
        print("Staff User")