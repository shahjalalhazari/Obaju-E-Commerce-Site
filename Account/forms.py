from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .models import User, Profile


#SIGNUP FORM
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


#CUSTOM PASSWORD RESET FORM
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="", required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': "Email"}))
    class Meta:
        model = User
        fields = ['email',]