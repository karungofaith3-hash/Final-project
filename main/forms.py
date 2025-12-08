from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        help_texts = {
            'username': '',  # Remove verbose help text
        }
        labels = {
            'email': 'Email Address',
        }
