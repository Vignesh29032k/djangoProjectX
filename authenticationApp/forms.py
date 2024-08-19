
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

#create/register a User (Model Form)

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
        


# Authenticate a User (Model Form)

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# Update UserForm
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']







