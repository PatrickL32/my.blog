# accounts/views.py

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    # Use your custom form, not the default one
    form_class = CustomUserCreationForm
    
    # Redirect to the login page after a successful signup
    success_url = reverse_lazy('login')
    
    # Specify the template to use
    template_name = 'registration/signup.html'

