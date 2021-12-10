from app.models import Contacto, Marca, Producto
from django.contrib import admin

# Register your models here.}


class ProductoAdmin(admin.ModelAdmin):
    list_display=['nombre','precio','nuevo','marca']
    list_editable=['precio']
    search_fields=['nombre']
    list_filter=['marca','nuevo','precio']
    list_per_page=5 #5 registros por pagina 
    
admin.site.register(Marca)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Contacto)