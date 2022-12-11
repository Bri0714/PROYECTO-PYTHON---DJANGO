"""proyectofinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views




urlpatterns = [
    
    path("", views.mostrar_index,name="Home"),
    path("mostrar_conductor_html/", views.mostrar_conductor_html, name="Mostrar"),
    path("crear_conductor/", views.crear_conductor, name="conductor"),
    path("crear_empresa/", views.crear_empresa, name = "empresa"),
    path("crear_ruta/", views.crear_ruta, name = "ruta"),
    path("buscar_conductor/", views.buscar_conductor, name = "buscar_conductor"),
    path("buscar_ruta/", views.buscar_ruta, name = "buscar_ruta"),
    path("buscar_empresa/", views.buscar_empresa, name = "buscar_empresa"),
    path("eliminar_conductor/<conductor_id>", views.eliminar_conductor, name = "eliminar_conductor"),
    path("actualizar_conductor/<conductor_id>", views.actualizar_conductor, name = "actualizar_conductor"),
    path("empresa_list/", views.EmpresaList.as_view(), name = "List"),
    path("empresa_detail/<pk>", views.EmpresaDetail.as_view(), name = "Detail"),
    path("eliminacion_confirmar/<pk>", views.EmpresaDeleteView.as_view(), name = "Delete"),
    path("signup/", views.SignUpView.as_view(), name = "Sign Up"),
    path("login/", views.AdminLoginView.as_view(), name = "Login"),
    path("logout/", views.AdminLogoutView.as_view(), name = "Logout")
]
