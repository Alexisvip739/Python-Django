from django.db import models
from django.db.models.base import Model

# Create your models here.

class Persona(models.Model):

    id=models.AutoField(primary_key=True) #autoincremental 
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=120)
    correo = models.EmailField(max_length=200)

    def __str__(self):
        return  self.nombre+" "+ self.apellido

 