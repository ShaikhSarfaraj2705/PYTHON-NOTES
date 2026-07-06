# =====================================================
# ROUTER CONFIGURATION
# =====================================================

from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

# Create Router
router = DefaultRouter()

# Register ViewSet
router.register(
    "students",
    StudentViewSet,
    basename="student"
)

# Generate URL Patterns
urlpatterns = router.urls