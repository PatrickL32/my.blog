from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    template_name = "registration/sigup.html"
    form_class = UserCreationForm
    Success_url = reverse_lazy("login")
