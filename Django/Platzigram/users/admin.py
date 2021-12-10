from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import Profile
# Register your models here.
@admin.register(Profile) ## manda el modelo de la persona registrada a la pagina

# nos muestra nuestro perfil a ingresar como superuser en la pagina de django
class ProfileAdmin(admin.ModelAdmin):
    """profile admin"""
    list_display=('pk','user','phone_number','website','picture')# despliega la informacion en este orden
    list_display_links=('pk','user','phone_number')
    search_fields=('user__email','user__first_name','user__username')
    list_filter=('created','modified')
    
    # nos ordena los datos con  respecto a como quieren que se muestre
    fieldsets=(
        ('Profile',{
            'fields':('user','picture'),
        
        }),
        ('Informacion Etra sobre user',{
            'fields':(
                ('website','phone_number'),
                ('biography')
            )        
        }),
        ('Metadatos',{
            'fields':(
                (('created','modified'))
            )
        })
    )
    readonly_fields=('created','modified')


# esto nos ayuda agregar un usuariio dentro de el modelo de Profile para asi no estar caambiando de pagina
class ProfileInline(admin.StackedInline):
    # de que modelo es 
    model=Profile
    verbose_name_plural='profiles'
class UserAdmin(BaseUserAdmin):
    #agrega el perfil del admin a una base de usuario
    inlines=(ProfileInline,)
    list_display=('username','email','first_name','last_name','is_active','is_staff')

admin.site.unregister(User)
admin.site.register(User,UserAdmin)



   

