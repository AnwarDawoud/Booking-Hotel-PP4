# hotels_booking/hotel_your_choice/forms.py

from django.contrib.auth.forms import UserCreationForm
from django import forms
from allauth.account.forms import SignupForm, LoginForm


class CustomLoginForm(LoginForm):
    # Add custom fields or overrides if needed
    pass


class CustomUserCreationForm(UserCreationForm):
    # Add custom fields or override existing ones if needed
    class Meta(UserCreationForm.Meta):
        pass
