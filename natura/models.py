from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=250)
    descripcion = models.TextField(max_length=1000)
    precio = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    publicado = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="publicado")
    imagen = models.ImageField(upload_to='productos')

    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.categoria}'

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile')
    imagen = models.ImageField(upload_to='profiles')
    
    def __str__(self):
        return f'{self.id} - {self.user}' 

class Mensaje(models.Model):
    mensaje = models.TextField(max_length=1000)
    email = models.EmailField()
    destinatario = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='destinatario')