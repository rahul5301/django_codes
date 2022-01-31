from statistics import mode
from attr import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from importlib_metadata import email
from sqlalchemy import true
from myapp2.models import *


class Newuserform(UserCreationForm):
    email= forms.EmailField(required=True)
    class Meta:
        model=User
        fields=('username','email','password1','password2')

    def save(self, commit=True):
        user=super(Newuserform,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user
class Employeeform(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'