from django.db import models

# Create your models here.

class conductor(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    celular = models.IntegerField()
    edad = models.IntegerField()
    

class ruta(models.Model):
    
    number = models.IntegerField(null=True)
    placa = models.CharField(max_length=40, null=True)
    

class empresa(models.Model):
    
    nombre = models.CharField(max_length=70)