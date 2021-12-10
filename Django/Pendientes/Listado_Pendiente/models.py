from django.db import models

# Create your models here.
class Pendientes(models.Model):
    id=models.AutoField(primary_key=True)
    Titulo=models.CharField(max_length=20)
    Descripcion=models.CharField(max_length=100)
    Horario=models.TimeField()

    def __str__(self):
        return "ID: "+str(self.pk)+"  "+self.Titulo
    

