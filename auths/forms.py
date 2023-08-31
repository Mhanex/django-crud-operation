from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput



class RegistrationForm(UserCreationForm):

    username = forms.CharField(
        label="Choose Username", 
        help_text="", widget=forms.TextInput(attrs={'autocomplete': 'off'})
        )
    password1 = forms.CharField(
        label="Create Password", 
        strip=False,  
        help_text="Note: password must be at least 8 characters e.g test$#12",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'})
        )
    password2 = forms.CharField(
        label="Confirm your password", 
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'})
        )
    
    class Meta:
        model = User
        fields = ['username', 'password1','password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'autocomplete': 'off'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'off'}),
    )
