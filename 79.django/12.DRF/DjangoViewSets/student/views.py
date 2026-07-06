# =====================================================
# MODEL VIEWSET
# =====================================================

from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):

    # Data Source
    queryset = Student.objects.all()

    # Serializer
    serializer_class = StudentSerializer