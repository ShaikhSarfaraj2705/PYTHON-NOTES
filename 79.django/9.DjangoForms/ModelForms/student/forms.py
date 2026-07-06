# =====================================================
# MODEL FORM
# =====================================================

from django import forms
from .models import Student

class StudentModelForm(forms.ModelForm):

    class Meta:

        # Model used to create the form
        model = Student

        # Include all model fields
        fields = "__all__"

        # OR choose specific fields
        # fields = ["name", "age", "email", "city"]