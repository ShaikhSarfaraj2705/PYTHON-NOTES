# =====================================================
# MODEL SERIALIZER
# =====================================================

from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:

        # Model to Serialize
        model = Student

        # Include all model fields
        fields = "__all__"

        # OR

        # fields = (
        #     "id",
        #     "name",
        #     "age",
        #     "email",
        #     "city"
        # )

        # Validate Age
    def validate_age(self, value):

        if value < 18:

            raise serializers.ValidationError(
                "Age must be at least 18."
            )

        return value