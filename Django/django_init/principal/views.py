from django.forms.forms import Form
from django.shortcuts import redirect, render

# Create your views here.

from .models import Persona
from .forms import personaForm
def inicio(request):
    personas=Persona.objects.all() #select * from persona
    contexto={
        'personas':personas
    }
    return render(request,'index.html',contexto)

def crearPersona(request):
    if request.method=='GET':

        form=personaForm()
        contexto={
            'form':form
        }
    else:
        form=personaForm(request.POST)
        contexto={
            'form':form
        }

        if form.is_valid(): # esto nos indica que se almasenara los valores en la base de datos
            form.save()
            return redirect('index')
    return render(request,'crear.html',contexto)

def editarPersona(request,id):
    persona=Persona.objects.get(id=id)
    if request.method=='GET':
        form=personaForm(instance=persona)
        contexto={
            'form':form
        }
    else:
        form=personaForm(request.POST,instance=persona) # nos indica que se esta tomando una instancia creada y no como una nueva
        contexto={
            'form':form
        }
        if form.is_valid(): # esto nos indica que se almasenara los valores en la base de datos
            form.save()
            return redirect('index')    
    return render(request,'crear.html',contexto)

def eliminarPersona(request,id):
    persona=Persona.objects.get(id=id)
    persona.delete()
    return redirect('index')