"""
URL configuration for QuerySets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("all/", views.all_students),
    path("filter/", views.filter_students),
    path("exclude/", views.exclude_students),
    path("get/", views.get_student),
    path("first/", views.first_student),
    path("last/", views.last_student),
    path("ascending/", views.ascending_students),
    path("descending/", views.descending_students),
    path("count/", views.count_students),
    path("exists/", views.student_exists),
    path("values/", views.values_students),
    path("valueslist/", views.values_list_students),
    path("multiple/", views.multiple_filter),
    path("lookup/", views.lookup_examples),

]
