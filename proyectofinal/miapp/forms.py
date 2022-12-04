from django import forms

class crearempresaform(forms.Form):
    
    nombre = forms.CharField(max_length=40)

class crearconductorform(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    celular = forms.IntegerField()
    edad = forms.IntegerField()


class crearrutaform(forms.Form):
    
    number = forms.IntegerField()
    placa = forms.CharField(max_length=40)
    