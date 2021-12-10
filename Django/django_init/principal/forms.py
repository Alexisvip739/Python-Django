from django import forms
from django.forms import fields, models
from .models import Persona

class personaForm(forms.ModelForm):
    class Meta:
        model=Persona
        fields= '__all__'
        