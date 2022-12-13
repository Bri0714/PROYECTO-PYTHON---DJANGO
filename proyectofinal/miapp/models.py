from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta, timezone, tzinfo

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
    
    number = models.IntegerField()
    placa = models.CharField(max_length=40)
    conductor = models.ForeignKey(conductor, on_delete=models.CASCADE, default=1)

    
    def __str__(self) :
        return f"Ruta  de placa: { self.placa}, con numero {self.number}.   Conductor: {self.conductor}"


class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to = "images/", null = True, blank=True)

    def __str__(self) :
        return f"Avatar: { self.user} imagen : {self.imagen}, de Bogota DC."



class Comment(models.Model):
    
    conductor = models.ForeignKey(conductor, on_delete=models.CASCADE, default=1)
    author = models.CharField(max_length=40)
    text = models.TextField()
    created_date = models.DateTimeField(default=datetime.now())
    approved_comment = models.BooleanField(default=False)
    Imagen = models.ImageField(upload_to="Pruebas", null=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text