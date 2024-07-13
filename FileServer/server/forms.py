from django.contrib.auth.models import User
from django import forms
from .models import Document
from custom_user.models import User as custom_user_model
from allauth.account.forms import SignupForm, LoginForm

class CustomSignUpForm(SignupForm):
    email = forms.EmailField(max_length=254, required=True, label='Email Address', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@gmail.com'}))
    password1 = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password Confirmation', required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    def save(self, request):
        user = super(CustomSignUpForm, self).save(request)
        user.save()
        return user
    
class CustomLoginForm(LoginForm):
    login = forms.EmailField(max_length=254, required=True, label='Email Address', widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    remember = forms.BooleanField(label='Remember Me', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

class DocumentUploadForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['title', 'description', 'file']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Title of document'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control mb-3',
                'rows': 5,
                'cols': 25,
                'placeholder': 'Provide a brief description'
            }),
            'file': forms.FileInput(attrs={
                'class': 'form-control mb-3'
            })
            
        }

class EmailSendForm(forms.Form):
    recipient_email = forms.EmailField(
        label='Recipient Email',
          required=True, 
          widget=forms.TextInput(attrs={
              'class': 'form-control my-2',
              'type': 'email',
              'placeholder': 'example@gmail.com'
          }))
    