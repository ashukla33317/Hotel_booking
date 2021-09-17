from django import forms
from django.forms import widgets


class Login_form(forms.Form):
    user_name=forms.CharField(max_length=20)
    password = forms.CharField(widget = forms.PasswordInput())