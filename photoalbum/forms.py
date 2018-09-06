from django import forms
from django.core.exceptions import ValidationError
from photoalbum.models import Photo, User
from django.core.validators import EmailValidator
from .validators import validate_login


class LoginForm(forms.Form):
    login = forms.CharField(label='login', max_length=64)
    password = forms.CharField(label='hasło', max_length=64, widget=forms.PasswordInput)


class AddUserForm(forms.Form):
    login = forms.EmailField(label='Login(email)', validators=[EmailValidator, validate_login])
    password = forms.CharField(max_length=64, label='Hasło', widget=forms.PasswordInput)
    password_repeat = forms.CharField(max_length=64, label='Powtórz hasło', widget=forms.PasswordInput)

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['password_repeat']:
            raise ValidationError('Niepoprawne hasło')

