from Listado_Pendiente.models import Pendientes
from django import forms
from django.forms import fields,models
from .models import Pendientes

class PendienteForms(forms.ModelForm):
    class Meta:
        model=Pendientes
        fields='__all__'