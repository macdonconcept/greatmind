from django import forms 
from .models import *
from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class contactform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'message']

class CustomerForm(UserCreationForm):
    class Meta:
        model= User
        fields =['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class Profileupdateform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'pix']