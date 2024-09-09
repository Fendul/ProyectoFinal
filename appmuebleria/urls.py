from django.urls import path
from appmuebleria.views import *

urlpatterns = [
    
    path('',inicio, name="Inicio"),
    path("inicio/", inicio, name="inicio"),
    path("catalogo/", catalogo, name="catalogo"),
    
    #CLIENTES
    path("clientes/nuevo", ClienteCreateView.as_view() , name= "nuevoCliente"),
    path("clientes/lista", ClienteListView.as_view(), name="leerClientes"),
    path("clientes/<pk>", ClienteDetailView.as_view() , name= "detalleCliente"),
    path("clientes/<pk>/editar", ClienteUpdateView.as_view() , name= "editarCliente"),
    path("clientes/<pk>/borrar", ClienteDeleteView.as_view() , name= "borrarCliente"),
    
    #VENDEDORES
    path("vendedores/nuevo", VendedorCreateView.as_view() , name= "nuevoVendedor"),
    path("vendedores/lista", VendedorListView.as_view(), name="leerVendedores"),
    path("vendedores/<pk>", VendedorDetailView.as_view() , name= "detalleVendedor"),
    path("vendedores/<pk>/editar", VendedorUpdateView.as_view() , name= "editarVendedor"),
    path("vendedores/<pk>/borrar", VendedorDeleteView.as_view() , name= "borrarVendedor"),
    
    #PRODUCTOS
    path("productos/nuevo", ProductoCreateView.as_view() , name= "nuevoProducto"),
    path("productos/lista", ProductoListView.as_view(), name="leerProductos"),
    path("productos/<pk>", ProductoDetailView.as_view() , name= "detalleProducto"),
    path("productos/<pk>/editar", ProductoUpdateView.as_view() , name= "editarProducto"),
    path("productos/<pk>/borrar", ProductoDeleteView.as_view() , name= "borrarProducto"),
        
]