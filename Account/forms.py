from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django_countries.widgets import CountrySelectWidget
from django_countries import countries
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


#PROFILE FORM
COUNTRY_CHOICES = tuple(countries)

class ProfileForm(forms.ModelForm):
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, label="Country", required=False)
    class Meta:
        model = Profile
        fields = ['fullname', 'address', 'city', 'state', 'zipcode', 'country', 'phone']
        widgets = {'country': CountrySelectWidget()}