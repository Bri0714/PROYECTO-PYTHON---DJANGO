from django.shortcuts import render
from django.http import HttpResponse
from miapp.models import conductor,empresa,ruta
from miapp.forms import crearempresaform, crearrutaform,crearconductorform



def mostrar_conductor_html(request):


        conductores = conductor.objects.all()
        context = {"conductores": conductores}
        #conductor2 = conductor(nombre = "andrea", apellido = "amezquita", celular = "312789456", edad = 31)
        #return render(request, "mostrar_conductor.html", {"nombre" : conductor1.nombre, "apellido" :conductor1.apellido, "celular" : conductor1.celular, "edad" : conductor1.edad})
        
        return render(request, "mostrar_conductor.html", context=context)



def mostrar_index(request):

        return render(request, "index.html")



def crear_conductor(request):

        if request.method == "POST":

                formulario = crearconductorform(request.POST)
                
                if formulario.is_valid():
                        
                        formulario_limpio = formulario.cleaned_data
                        
                        conductores = conductor(nombre=formulario_limpio["nombre"], apellido=formulario_limpio["apellido"],celular=formulario_limpio["celular"],edad=formulario_limpio["edad"],empresa=formulario_limpio["empresa"])
                        
                        conductores.save()
                
                return render(request, "index.html")

        else:
                
                formulario = crearconductorform()

        return render(request, "crear_conductor.html", {"formulario" : crearconductorform } )



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

def buscar_empresa(request):
        
        if request.GET.get("nombre" , False):
                apellido = request.GET["nombre"]
                empresas = ruta.objects.filter(nombre__icontains=apellido)
                
                return render(request, "buscar_empresa.html", {"empresas" : empresas})
        else:
                respuesta = "no hay datos"
        
        return render(request, "buscar_empresa.html", {"respuesta" : respuesta} )


def eliminar_conductor(request, conductor_id):

        conductores = conductor.objects.get( id = conductor_id)

        conductores.delete()

        conductores = conductor.objects.all()
        context = {"conductores": conductores}
        
        return render(request, "mostrar_conductor.html", context=context)