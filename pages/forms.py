

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
User = get_user_model()


class LoginForm(forms.Form):  # 16 user Login
    username = forms.CharField(label='',required=True,
        widget = forms.TextInput(attrs={
            'type': 'text','class': 'form-control',# 'size': '8',
             'placeholder': 'enter user name'}))

    password = forms.CharField(label='',required=True,
        widget=forms.PasswordInput(
            attrs={ 'placeholder': 'Password','class': 'form-control', }))
