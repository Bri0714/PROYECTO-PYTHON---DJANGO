from django.db import models

# Create your models here.

class empresa(models.Model):
    
    nombre = models.CharField(max_length=70)

class conductor(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    celular = models.IntegerField()
    edad = models.IntegerField()
    empresa =  models.ForeignKey(empresa, on_delete=models.CASCADE, default=1)
    

class ruta(models.Model):
    
    number = models.IntegerField(null=True)
    placa = models.CharField(max_length=40, null=True)
    