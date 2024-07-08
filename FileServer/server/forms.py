from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from custom_user.models import User as custom_user_model


class SignUpForm(UserCreationForm):
    
    class Meta:
        model = custom_user_model
        fields = ['email', 'password1', 'password2']