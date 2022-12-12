from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class empresa(models.Model):
    
    nombre = models.CharField(max_length=40)

    def __str__(self) :
        return f" {self.nombre}, Bogota DC."

class conductor(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    celular = models.IntegerField()
    edad = models.IntegerField()
    empresa =  models.ForeignKey(empresa, on_delete=models.CASCADE, default=1)

    def __str__(self) :
        return f"Nombre: { self.nombre}, Apellido: {self.apellido}, Celular: {self.celular},Edad: {self.edad},Empresa: {self.empresa}"
    

class ruta(models.Model):
    
    number = models.IntegerField(null=True)
    placa = models.CharField(max_length=40, null=True)
    
    def __str__(self) :
        return f"Ruta  de placa: { self.placa},con numero {self.number},de Bogota DC."


class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to = "images/", null = True, blank=True)