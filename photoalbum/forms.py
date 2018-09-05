from django import forms
from django.core.exceptions import ValidationError
from photoalbum.models import Photo


class LoginForm(forms.Form):
    login = forms.CharField(label='login', max_length=64)
    password = forms.CharField(label='hasło', max_length=64, widget=forms.PasswordInput)





