from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.TextField(max_length=250)
        
    def __str__(self):
        return f'{self.nombre} - {self.categoria}'


class Consultora(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    codigoCN = models.IntegerField(max_length=7)
    zona = models.CharField(max_length=100)
    
    def __str__(self):
        return f'Consultora: {self.nombre} {self.apellido} CN: {self.codigoCN}'


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    pedido = models.TextField(max_length=500)
    consultora = models.CharField(max_length=200)
    
    def __str__(self):
        return f'Pedido n°{self.id}. Cliente: {self.nombre} {self.apellido}. Consultora: {self.consultora}'