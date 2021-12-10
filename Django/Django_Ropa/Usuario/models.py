from django.db import models

# Create your models here.
datos_marca=[
    [0,'Nike'],
    [1,'Gucci'],
    [2,'Adidas'],
    [3,'Louis Vuitton'],
    [4,'Cartier'],
    [5,'Zara'],
    [6,'H&M']
]
class AgregarProducto(models.Model):
    Nombre=models.CharField(max_length=50)
    Precio=models.IntegerField()
    Preferencia=models.IntegerField(choices=datos_marca)
    Imagen=models.ImageField(upload_to='productos',null=False)

    def __str__(self) -> str:
        return self.Nombre

    