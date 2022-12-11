from django import forms
from miapp import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class crearempresaform(forms.Form):
    
    nombre = forms.CharField(max_length=40)

class crearconductorform(forms.ModelForm):
    
    class Meta:
        model = models.conductor
        fields = [
            'nombre',
            'apellido',
            'celular',
            'edad',
            'empresa'
        ]

class crearrutaform(forms.Form):
    
    number = forms.IntegerField()
    placa = forms.CharField(max_length=40)
    

class SignUpForm(UserCreationForm):

    class Meta:

        model = User
        fields = [
            
            "username",
            "email",
            "password1",
            "password2"
        ]
        
