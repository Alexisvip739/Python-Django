from django.contrib import admin
from django.contrib.auth import authenticate, login
from Usuario.models import AgregarProducto
from django.http import request
from Usuario.forms import CustomUserCreationForm, ProductosForm
from django.shortcuts import get_object_or_404, render,redirect

def Inicio(request):
    formulario=AgregarProducto.objects.all()
    data={'form':formulario}
    return render(request,'app/index.html',data)

def Listado(request):
    formulario=AgregarProducto.objects.all()
    data={'form':formulario}
    return render(request,'app/Listado.html',data)

def Post(request):
    data={'form':ProductosForm()}
    if request.method=='POST':
        formulario=ProductosForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']='contacto Guardado'
        else:
            data['form']=formulario
        
    return render(request,'app/Post.html',data)

def Editar(request,id):
    formulario=get_object_or_404(AgregarProducto,id=id)
    data={'form':ProductosForm(instance=formulario)}
    if request.method=='POST':
        producto=ProductosForm(request.POST,instance=formulario,files=request.FILES)
        if producto.is_valid():
            producto.save()
            return redirect(to='Listado')
        data['form']=producto
    return render(request,'app/Editar.html',data)
        
def Eliminar(request,id):
    formulario=get_object_or_404(AgregarProducto,id=id)
    formulario.delete()
    return redirect(to='Listado')

def Registrar(request):
    data={'form':CustomUserCreationForm}
    if request.method=='POST':
        formulario=CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.changed_data["username"],password=formulario.changed_data['password1'])
            login(request,user)
            return redirect(to='home')
        data['form']=formulario
    return render(request,'registration/registro.html',data)