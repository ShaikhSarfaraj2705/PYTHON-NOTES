# =====================================================
# MODEL SERIALIZER
# =====================================================

from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:

        # Model to serialize
        model = Student

        # Include all fields
        fields = "__all__"

    # Custom Validation
    def validate_age(self, value):

        if value < 18:

            raise serializers.ValidationError(
                "Age must be at least 18."
            )

        return value