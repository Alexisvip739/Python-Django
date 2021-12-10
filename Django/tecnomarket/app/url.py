from app.views import agregarProducto, contacto, eliminar_producto, galeria, home, listar_producto, modificar_producto, registro
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',home,name='home'),
    path('contacto/',contacto,name='contacto'),
    path('galeria/',galeria,name='galeria'),
    path('agregar/',agregarProducto,name='agregar_producto'),
    path('listar-producto/',listar_producto,name='listar_productos'),
    path('modificar-producto/<id>',modificar_producto,name='modificar_producto'),
    path('eliminar_producto/<id>',eliminar_producto,name='eliminar_producto'),
    path('registro/',registro,name='registro')
]
