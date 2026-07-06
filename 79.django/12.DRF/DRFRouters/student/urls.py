# =====================================================
# DEFAULT ROUTER
# =====================================================

from rest_framework.routers import DefaultRouter

from .views import StudentViewSet

router = DefaultRouter()

# Register ViewSet
router.register(

    "students",

    StudentViewSet,

    basename="student"

)

urlpatterns = router.urls