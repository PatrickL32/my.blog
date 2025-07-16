from django.contrib.auth.forms import(
UserCreationForm,
UserChangeForm
)
from .models import CustomUser


class CustomuUserCreationForm(UserCreationForm):
    class  Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields  + ("username","email","role")

    class CustomUserChangeForm(UserChangeForm):
        class meta(UserChangeForm):
            model=CustomUser
            fields = UserChangeForm.Meta.fields + ("username","email","role")