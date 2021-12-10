from django.contrib.auth.models import User
from users import models
from django import forms
from django.forms.fields import CharField, ImageField

from users.models import Profile
## este nos ayudara a saber la longitud de el campo de texto al momento de  validar la informacion a manipular 
class ProfileForm(forms.Form):
    website=forms.URLField(max_length=200, required=True)
    biography= forms.CharField(max_length=500, required=False)
    phone_number=forms.CharField(max_length=20, required=False)
    picture= forms.ImageField()


class SignupForm(forms.Form): 
    usernamme=forms.CharField(min_length=4, max_length=50)
    password=forms.CharField(max_length=70,widget=forms.PasswordInput())
    password_confirmation=forms.CharField(max_length=70,widget=forms.PasswordInput())
    first_name=forms.CharField(min_length=2,max_length=50)
    last_name=forms.CharField(min_length=2,max_length=50)
    email=forms.CharField(min_length=6,max_length=70,widget=forms.EmailInput())
    
    
    def clean_username(self):# el usuario solamente puede ser unico 
        username=self.cleaned_data['username'] # datos que estan en el diccionario de django 
        username_taken=User.objects.filter(username=username).exists() #trae todos los usuarios que exiten
        if username_taken:
            raise forms.ValidationError('Username is already in use')
        return username

    def clean(self):
        data=super().clean()
        password=data['password']
        password_confirmation=['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('Password do not match')
        return data

    def safe(self):
        # crea un usuario y perfil
        data= self.cleaned_data
        data.pop('password_confirmation')
        user=User.objects.create_user(**data)

        profile=Profile(user=user)
        profile.save()
