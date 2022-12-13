from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from miapp.models import conductor,empresa,ruta,Avatar,Comment
from .forms import crearempresaform, crearrutaform,crearconductorform,SignUpForm,UserEditForm,crearcomentarioform
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def mostrar_conductor_html(request):


        conductores = conductor.objects.all()
        context = {"conductores": conductores}
        #conductor2 = conductor(nombre = "andrea", apellido = "amezquita", celular = "312789456", edad = 31)
        #return render(request, "mostrar_conductor.html", {"nombre" : conductor1.nombre, "apellido" :conductor1.apellido, "celular" : conductor1.celular, "edad" : conductor1.edad})
        
        return render(request, "mostrar_conductor.html", context=context)


@login_required
def mostrar_index(request):

        imagenes = Avatar.objects.filter(user = request.user.id)

        return render(request, "index.html", {"url": imagenes[0].imagen.url})


@login_required
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


@login_required
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

@login_required
def crear_ruta(request):


        if request.method == "POST":

                formulario = crearrutaform(request.POST)
                
                if formulario.is_valid():
                        
                        formulario_limpio = formulario.cleaned_data
                        
                        ruta1 = ruta( number=formulario_limpio["number"], placa=formulario_limpio["placa"], conductor =formulario_limpio["conductor"] )
                        
                        ruta1.save()
                
                return render(request, "index.html")

        else:
                
                formulario = crearrutaform()

        return render(request, "crear_ruta.html", {"formulario" : crearrutaform } )

@login_required
def buscar_conductor(request):
        
        if request.GET.get("apellido" , False):
                apellido = request.GET["apellido"]
                conductores = conductor.objects.filter(apellido__icontains=apellido)
                
                return render(request, "buscar_conductor.html", {"conductores" : conductores})
        else:
                respuesta = "no hay datos"
        
        return render(request, "buscar_conductor.html", {"respuesta" : respuesta} )

@login_required
def buscar_ruta(request):
        
        if request.GET.get("placa", False):
                
                placa = request.GET["placa"]
                rutas = ruta.objects.filter(placa__icontains = placa).values()

                print(rutas[0]['id'])
                conductores = conductor.objects.filter(ruta=rutas[0]['id'])
                print(conductores)
                
                return render(request, "buscar_ruta.html", {"rutas" : rutas, "conductores" : conductores})
        else:
                respuesta = "no hay datos"
        
        return render(request, "buscar_ruta.html", {"respuesta" : respuesta} )

@login_required
def buscar_empresa(request):
        
        if request.GET.get("nombre_empresa", False):
                
                nombre_empresa = request.GET["nombre_empresa"]
                empresas = empresa.objects.filter(nombre__icontains = nombre_empresa).values()

                print(empresas[0]['id'])
                conductores = conductor.objects.filter(empresa=empresas[0]['id'])
                print(conductores)
                
                return render(request, "buscar_empresa.html", {"empresas" : empresas, "conductores" : conductores})
        else:
                respuesta = "no hay datos"
        
        return render(request, "buscar_empresa.html", {"respuesta" : respuesta} )



@login_required
def eliminar_conductor(request, conductor_id):

        conductores = conductor.objects.get( id = conductor_id)

        conductores.delete()

        conductores = conductor.objects.all()
        context = {"conductores": conductores}
        
        return render(request, "mostrar_conductor.html", context=context)


@login_required
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


class EmpresaList(LoginRequiredMixin,ListView):
        
        template_name = "MiApp/empresas_list.html"
        model: empresa

        def get_queryset(self):
                return empresa.objects.all()

class EmpresaDetail(LoginRequiredMixin,DetailView):
        
        template_name = "MiApp/empresas_detalle.html"
        model: empresa

        def get_queryset(self):
                return empresa.objects.all()

class EmpresaDeleteView(LoginRequiredMixin,DeleteView):

        model: empresa
        success_url = "/empresa_list"

        def get_queryset(self):
                return empresa.objects.all()


class SignUpView(CreateView):

        form_class: SignUpForm
        success_url = reverse_lazy("Login")
        template_name = "registro.html"

                
        def get_form_class(self):
                return SignUpForm
        

class AdminLoginView(LoginView):

        template_name = "login.html"

class AdminLogoutView(LoginRequiredMixin,LogoutView):

        template_name = "logout.html"


@login_required
def editar_usuario(request):

        usuario = request.user

        if request.method == "POST":

                usuario_form = UserEditForm(request.POST)

                if usuario_form.is_valid():

                        informacion = usuario_form.cleaned_data

                        usuario.username = informacion["username"]
                        usuario.email = informacion["email"]
                        usuario.password1 = informacion["password1"]
                        usuario.password2 = informacion["password2"]

                        usuario.save()
                
                return render(request, "index.html" )

        else:
                usuario_form = UserEditForm(initial={
                        "username": usuario.username,
                        "email": usuario.email,

                })
        return render(request, "Miapp/admin_update.html", {
                
                "form" : usuario_form,
                "usuario" : usuario
        } )


@login_required
def post_details(request):

        if request.method == "POST":

                formulario = crearcomentarioform(request.POST)
                
                if formulario.is_valid():
                        
                        formulario_limpio = formulario.cleaned_data
                        
                        comentarios1 = Comment(conductor=formulario_limpio["conductor"], author=formulario_limpio["author"],text=formulario_limpio["text"],created_date=formulario_limpio["created_date"])
                        
                        comentarios1.save()
                
                return render(request, "index.html")

        else:
                
                formulario = crearcomentarioform()

        return render(request, "post_details.html", {"formulario" : crearcomentarioform } )

@login_required
def mostrar_comentarios(request):


        comentarios = Comment.objects.all()
        context = {"comentarios": comentarios }

        return render(request, "mostrar_comentarios.html", context=context)