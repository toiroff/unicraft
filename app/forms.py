from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Certificates


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'password1', 'password2']


class CertificatesForm(forms.ModelForm):
    class Meta:
        model = Certificates
        fields = '__all__'
        exclude = ['user']