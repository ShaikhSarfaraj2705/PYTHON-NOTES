# =====================================================
# PROJECT URLS
# File: FirstProject/urls.py
# =====================================================

from django.contrib import admin
from django.urls import path, include
from student import views
from user import views


urlpatterns = [

    # Admin Panel
    path('admin/', admin.site.urls),

    # Home Page
    path('', views.home),

    # All URLs starting with 'student/'
    # are handled by student/urls.py
    path('student/', include('student.urls')),


    ###URL with Parameters
    # Integer Parameter
    path('user/<int:id>/', views.user_detail),

    # String Parameter
    path('user/<str:name>/', views.user_profile),

]