from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile


#SIGNUP FORM
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']