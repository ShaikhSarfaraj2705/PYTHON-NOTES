# =====================================================
# File : student/forms.py
# =====================================================

from django import forms

class StudentForm(forms.Form):

    name = forms.CharField(max_length=100)
    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) < 3:
            raise forms.ValidationError(
                "Name must contain at least 3 characters."
            )
        return name

    age = forms.IntegerField()
    # Validate age field
    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 18:
            raise forms.ValidationError(
                "Age must be 18 or above."
            )
        return age

    email = forms.EmailField()

    city = forms.CharField(max_length=100)

    def clean(self):

        cleaned_data = super().clean()

        email = cleaned_data.get("email")

        city = cleaned_data.get("city")

        # Example validation
        if city == "Pune" and not email.endswith("@gmail.com"):

            raise forms.ValidationError(
                "Pune users must use Gmail."
            )

        return cleaned_data