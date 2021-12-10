import django
from Usuario.models import AgregarProducto
from django import forms
from django.forms import fields, models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ProductosForm(forms.ModelForm):
    class Meta:
        model=AgregarProducto
        fields='__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','password1','password2','email']
