from django import forms

class crearrutaform(forms.Form):
    
    number = forms.IntegerField()
    placa = forms.CharField(max_length=40)
    

class crearempresaform(forms.Form):
    
    nombre = forms.CharField(max_length=40)