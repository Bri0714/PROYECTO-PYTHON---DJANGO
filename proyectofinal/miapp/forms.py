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

class crearrutaform(forms.ModelForm):
    
    class Meta:
        model = models.ruta
        fields = [
            'conductor',
            'placa',
            'number',
        ]

class SignUpForm(UserCreationForm):

    class Meta:

        model = User
        fields = [
            
            "username",
            "email",
            "password1",
            "password2"
        ]
        

class UserEditForm(UserCreationForm):

    class Meta:

        model = User
        fields = [
            
            "username",
            "email",
            "password1",
            "password2"
        ]

        help_texts = {k: "" for k in fields }

class crearcomentarioform(forms.ModelForm):
    
    class Meta:
        model = models.Comment
        fields = [
            'conductor',
            'author',
            'text',
            'created_date',
            "Imagen"
        ]

