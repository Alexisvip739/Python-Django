from Usuario.models import AgregarProducto
from django.contrib import admin

# Register your models here.

class Lista_Productos(admin.ModelAdmin):
    list_display=['Nombre','Precio','Preferencia']
    search_fields=['Nombre','Preferencia']
    list_editable=['Precio']

admin.site.register(AgregarProducto,Lista_Productos)