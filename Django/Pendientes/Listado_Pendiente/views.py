from django.http import request
from Listado_Pendiente.forms import PendienteForms
from django.forms.forms import Form

from .models import Pendientes
from django.shortcuts import render,redirect

# Create your views here.
def Listado_Pendiente(request):
    Mostrar_Listado=Pendientes.objects.all()
    if request.method=='POST':
        pass
    contexto={
       'mostrar':Mostrar_Listado 
    }
    return render(request,'Pendientes.html',contexto)

def Crear_Pendientes(request):
    if request.method=='GET':
        form=PendienteForms()
        contexto={
            'form':form
        }
    else:

        form=PendienteForms(request.POST)
        contexto={
            'form':form
        }
        if form.is_valid(): # esto nos indica que se almasenara los valores en la base de datos
            form.save()
            return redirect('Pendientes')
    return render(request,'CrearPendientes.html',contexto)

def Eliminar_Pendiente(request,id):
    persona=Pendientes.objects.get(id=id)
    persona.delete()
    return redirect('Pendientes')