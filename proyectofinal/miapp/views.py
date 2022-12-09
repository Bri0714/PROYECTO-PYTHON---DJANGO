from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
                        
                        conductor1 = conductor(nombre=formulario_limpio["nombre"], apellido=formulario_limpio["apellido"],celular=formulario_limpio["celular"],edad=formulario_limpio["edad"],empresa=formulario_limpio["empresa"])
                        
                        conductor1.save()
                
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
        
        if request.GET.get("empresa_id", False):
                
                empresa_id = request.GET["empresa_id"]
                empresas = empresa.objects.filter(id = empresa_id)
                #conductores = conductor.objects.filter(empresa_id=1)
                #conductores = conductor.objects.all
                return render(request, "buscar_empresa.html", {"empresas" : empresas})#,{"conductores" : conductores})
        else:
                respuesta = "no hay datos"
        
        return render(request, "buscar_empresa.html", {"respuesta" : respuesta} )




def eliminar_conductor(request, conductor_id):

        conductores = conductor.objects.get( id = conductor_id)

        conductores.delete()

        conductores = conductor.objects.all()
        context = {"conductores": conductores}
        
        return render(request, "mostrar_conductor.html", context=context)


def actualizar_conductor(request,conductor_id):

        conductor1 = conductor.objects.get( id = conductor_id)

        if request.method == "POST":

                formulario = crearconductorform(request.POST)
                
                if formulario.is_valid():
                        
                        formulario_limpio = formulario.cleaned_data
                        
                        conductor1.nombre = formulario_limpio["nombre"]
                        conductor1.apellido = formulario_limpio["apellido"]
                        conductor1.celular = formulario_limpio["celular"]
                        conductor1.edad= formulario_limpio["edad"]

                        conductor1.save()
                
                return render(request, "index.html")

        else:
                
                formulario = crearconductorform(initial={"nombre":conductor.nombre,"apellido":conductor.apellido,"celular":conductor.celular,"edad":conductor.edad,})

        return render(request, "actualizar_conductor.html", {"formulario" : crearconductorform } )


class EmpresaList(ListView):
        
        template_name = "MiApp/empresas_list.html"
        model: empresa

        def get_queryset(self):
                return empresa.objects.all()

class EmpresaDetail(DetailView):
        
        template_name = "MiApp/empresas_detalle.html"
        model: empresa

        def get_queryset(self):
                return empresa.objects.all()

class EmpresaDeleteView(DeleteView):

        model: empresa
        success_url = "/empresa_list"

        def get_queryset(self):
                return empresa.objects.all()




