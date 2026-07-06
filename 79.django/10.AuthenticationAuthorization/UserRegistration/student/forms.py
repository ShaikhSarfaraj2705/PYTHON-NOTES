# =====================================================
# USER REGISTRATION FORM
# =====================================================

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    class Meta:

        # Built-in Django User model
        model = User

        # Fields displayed in registration form
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )