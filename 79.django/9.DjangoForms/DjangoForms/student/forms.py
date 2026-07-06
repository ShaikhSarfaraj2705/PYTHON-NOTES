# =====================================================
# File : student/forms.py
# =====================================================

from django import forms

class StudentForm(forms.Form):

    # Text Input
    # name = forms.CharField(max_length=100)
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Name"
            }
        )
    )


    # Number Input
    age = forms.IntegerField()

    # Custom Validation
    def clean_age(self):

        age = self.cleaned_data["age"]
        if age < 18:
            raise forms.ValidationError(
                "Age must be at least 18."
            )
        return age

    # Email Input
    # email = forms.EmailField()
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter Email"
            }
        )
    )

    # Text Input
    city = forms.CharField(max_length=100)