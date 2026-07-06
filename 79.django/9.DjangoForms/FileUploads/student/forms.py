from django import forms
from .models import Student

class UploadForm(forms.Form):

    # Upload a file
    file = forms.FileField()

class StudentForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = "__all__"