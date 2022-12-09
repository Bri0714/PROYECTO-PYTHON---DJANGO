from django import forms
from miapp import models

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
    