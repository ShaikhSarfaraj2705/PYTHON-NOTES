# =====================================================
# API VIEW
# =====================================================

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer


class StudentAPIView(APIView):

    # ===============================================
    # GET METHOD
    # ===============================================
    def get(self, request):

        # Get all students
        students = Student.objects.all()

        # Serialize QuerySet
        serializer = StudentSerializer(
            students,
            many=True
        )

        # Return JSON Response
        return Response(serializer.data)

    # ===============================================
    # POST METHOD
    # ===============================================
    def post(self, request):

        # Deserialize incoming JSON
        serializer = StudentSerializer(
            data=request.data
        )

        # Validate data
        if serializer.is_valid():

            # Save data into database
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        # Return validation errors
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )