from users.models import Profile
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)# cada que se borre el usuario se borre el posts
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='posts/photos')
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} by @{}'.format(self.title,self.user.username) ## nos ayuda a que las fotos ingresadas funcionen al querer verlas
        ## por tanto se agrega una rutas en el settings de la app de platzigram
    
