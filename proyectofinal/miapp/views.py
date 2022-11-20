from django.shortcuts import render
from django.http import HttpResponse
from miapp.models import conductor,empresa,ruta
from miapp.forms import crearempresaform, crearrutaform



def mostrar_conductor_html(request):


        conductor1 = conductor(nombre = "ricardo", apellido = "fernandez", celular = "3124715263", edad = 39)
        conductor2 = conductor(nombre = "andrea", apellido = "amezquita", celular = "312789456", edad = 31)
        #return render(request, "mostrar_conductor.html", {"nombre" : conductor1.nombre, "apellido" :conductor1.apellido, "celular" : conductor1.celular, "edad" : conductor1.edad})
        
        return render(request, "mostrar_conductor.html", {"conductores": [conductor1, conductor2]})


def mostrar_index(request):
    
        return render(request, "index.html")


def crear_conductor(request):
    
        if request.method == "POST":
            
            conductor1 = conductor(nombre=request.POST["nombre"], apellido=request.POST["apellido"], celular=request.POST["celular"], edad=request.POST["edad"])
            
            conductor1.save()
            
            return render(request, "index.html")
    
        return render(request, "crear_conductor.html")
    

def crear_empresa(request):
    
       
        if request.method == "POST":
    
                formulario = crearempresaform(request.POST)
                
                if formulario.is_valid():
                    
                    formulario_limpio = formulario.cleaned_data
                        
                    empresa1 = empresa(nombre=formulario_limpio["nombre"])
                    
                    empresa1.save()
            
                return render(request, "index.html")
        
        else:
            
            formulario = crearempresaform()
    
        return render(request, "crear_empresa.html", {"formulario" : formulario } )


def crear_ruta(request):
    
       
        if request.method == "POST":
    
                formulario = crearrutaform(request.POST)
                
                if formulario.is_valid():
                    
                    formulario_limpio = formulario.cleaned_data
                        
                    ruta1 = ruta( number=formulario_limpio["number"], placa=formulario_limpio["placa"])
                    
                    ruta1.save()
            
                return render(request, "index.html")
        
        else:
            
            formulario = crearrutaform()
    
        return render(request, "crear_ruta.html", {"formulario" : crearrutaform } )


def buscar_conductor(request):
        
        if request.GET.get("apellido" , False):
                apellido = request.GET["apellido"]
                conductores = conductor.objects.filter(apellido__icontains=apellido)
                
                return render(request, "buscar_conductor.html", {"conductores" : conductores})
        else:
                respuesta = "no hay datos"
        
        return render(request, "buscar_conductor.html", {"respuesta" : respuesta} )

def buscar_ruta(request):
        
        if request.GET.get("placa" , False):
                apellido = request.GET["placa"]
                rutas = ruta.objects.filter(placa__icontains=apellido)
                
                return render(request, "buscar_ruta.html", {"rutas" : rutas})
        else:
                respuesta = "no hay datos"
        
        return render(request, "buscar_ruta.html", {"respuesta" : respuesta} )