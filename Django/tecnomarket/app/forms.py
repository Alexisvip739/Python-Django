import django
from app.models import Contacto, Producto
from django import forms
from django.forms import fields, models, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ContactoForm(forms.ModelForm):
    class Meta:
        model=Contacto
        fields='__all__'
      

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model=Producto
        fields='__all__'

        widgets={
            'fecha_fabricacion':forms.SelectDateWidget()
        }

class CustomUserCreationForm(UserCreationForm): # este se crea a partir de el import de from django.contrib.auth.forms import UserCreationForm
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name','email','password1','password2']