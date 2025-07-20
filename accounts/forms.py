# accounts/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # Point to the custom user model
        model = get_user_model()
        # Add any other fields you want on the sign-up form
        fields = ('username', 'email')