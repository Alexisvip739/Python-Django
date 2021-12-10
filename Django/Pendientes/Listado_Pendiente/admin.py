from django.contrib import admin
from .models import Pendientes
# Register your models here.

class AdminPendiente(admin.ModelAdmin):
    list_display=["pk",'Titulo','Descripcion']
    list_filter=["Descripcion"]
    search_fields=["Titulo"]
    list_display_links=["pk","Titulo"]
admin.site.register(Pendientes,AdminPendiente)