# =====================================================
# File: student/urls.py
# =====================================================

from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.login),
    path('dashboard/', views.dashboard),

    #Redirect Using URL Name (Recommended)
    path('', views.home, name="home"),
    path('logout/', views.logout, name="logout"),

]