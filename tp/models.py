from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.forms import widgets
from django import forms

class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {'password': forms.PasswordInput}