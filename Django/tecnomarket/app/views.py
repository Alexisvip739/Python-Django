from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http.response import Http404
from app.forms import ContactoForm, CustomUserCreationForm, ProductoForm
from app.models import Producto
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
# Create your views here.


def home(request):
    productos=Producto.objects.all()
    data={
        'productos':productos
    }
    return render(request,'app/home.html',data)

def contacto(request):
    data={'form':ContactoForm()}
    if request.method=='POST':
        formulario=ContactoForm(request.POST, request.FILES)## enviaron datos
        if formulario.is_valid:
            formulario.save()
            data['mensaje']='contacto Guardado'
        else:
            data['form']=formulario   
    return render(request,'app/contacto.html',data)

def galeria(request):
    return render(request,'app/galeria.html')


def agregarProducto(request):
    data={
        'form':ProductoForm()
    }
    if request.method=='POST':
        formulario=ProductoForm(request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Agregado Correctamente')
        else:
            data['form']=formulario
    return render(request,'app/producto/agregar.html',data)


def listar_producto(request):
    productos=Producto.objects.all()
    page=request.GET.get('page',1)
    try:
        paginator=Paginator(productos,5)
        productos=paginator.page(page)
    except:
        raise Http404
    data={
        'entity':productos,
        'paginator':paginator
    }
    return render(request,'app/producto/listar.html',data)

def modificar_producto(request,id):
    producto=get_object_or_404(Producto,id=id)
    data={
        'form':ProductoForm(instance=producto)
    }
    if request.method=='POST':
        formulario=ProductoForm(request.POST,instance=producto,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'modificado correctamente')
            return redirect(to='listar_productos')
        data['form']=formulario

    return render(request,'app/producto/modificar.html',data)

def eliminar_producto(request,id):
    producto=get_object_or_404(Producto,id=id)
    producto.delete()
    messages.success(request,'Eliminado Correctamente')
    return redirect(to='listar_productos')

def registro(request):

    data={
        'form':CustomUserCreationForm
    }
    if request.method=='POST':
       formulario=CustomUserCreationForm(request.POST)
       if formulario.is_valid():
           formulario.save()
           user=authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
           login(request,user)
           messages.success(request,"Te haz registrado Correctamente")
           return redirect(to="home")
       data["form"]=formulario
       
    return render(request,'registration/registro.html',data)