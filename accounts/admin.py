from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm , CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form =CustomUserCreationForm
    form = CustomUserChangeForm
model=CustomUser
list_display =["email","username","role","is_staff"]
add_fieldsets = (
        (
            None, {
                "classes":("wide",),
                "fields":("email","role","password1","password2"),
            }
        ),
    )
fieldsets = UserAdmin.fieldsets + (
        (None,{"fields":("role",)})
    )

admin.site.register(CustomUser,CustomUserAdmin)
# Register your models here.
