# =====================================================
# JWT URLS
# =====================================================

from django.contrib import admin

from django.urls import include, path

from rest_framework_simplejwt.views import (

    TokenObtainPairView,

    TokenRefreshView,

)

urlpatterns = [

    path("admin/", admin.site.urls),

    path("api/", include("student.urls")),

    # Generate Access & Refresh Tokens
    path(

        "api/token/",

        TokenObtainPairView.as_view(),

        name="token_obtain_pair"

    ),

    # Refresh Access Token
    path(

        "api/token/refresh/",

        TokenRefreshView.as_view(),

        name="token_refresh"

    ),

]