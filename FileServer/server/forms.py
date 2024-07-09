from django.contrib.auth.models import User
from django import forms
from .models import Document
from django.contrib.auth.forms import UserCreationForm
from custom_user.models import User as custom_user_model


class SignUpForm(UserCreationForm):
    
    class Meta:
        model = custom_user_model
        fields = ['email', 'password1', 'password2']


class DocumentUploadForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['title', 'description', 'file']