from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
            attrs={'id': 'username', 'placeholder': 'Enter your User Name'}))
    email = forms.EmailField(widget=forms.EmailInput(
                attrs={'id': 'email', 'placeholder': 'Enter your Email'}),
                             required=True)
    password1 = forms.Field(widget=forms.PasswordInput(
                attrs={'id': 'password1', 'placeholder': 'Enter your Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
                attrs={'id': 'password2', 'placeholder': 'Confirm your Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    def clean_password1(self):  # Fixed method name
        password = self.cleaned_data.get('password1')  # Fixed field reference
        min_len = 8
        if password and len(password) < min_len:
            raise ValidationError(f'Password must be at least {min_len} characters long.')
        
        return password


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
                attrs={'id':'username', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
                attrs={'id':'password', 'placeholder':'Password'}))
