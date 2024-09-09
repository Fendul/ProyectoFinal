from appmuebleria.forms import *
from appmuebleria.models import *
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def inicio (request):
    
    return render (request, "appmuebleria/inicio.html")

def catalogo (request):
    
    return render (request, "appmuebleria/catalogo.html")

#VENDEDOR
class VendedorListView (LoginRequiredMixin, ListView):
    model = Vendedor
    context_object_name = "vendedores"
    template_name = "appmuebleria/vendedor_lista.html"
    
class VendedorDetailView(LoginRequiredMixin, DetailView):
    model = Vendedor
    template_name = "appmuebleria/vendedor_detalle.html"
    
class VendedorCreateView (LoginRequiredMixin, CreateView):
    model = Vendedor
    template_name = "appmuebleria/vendedor_crear.html"
    success_url = reverse_lazy("leerVendedores")
    fields = ["nombre", "cbu"]

class VendedorUpdateView (LoginRequiredMixin, UpdateView):
    model = Vendedor
    template_name = "appmuebleria/vendedor_editar.html"
    success_url = reverse_lazy("leerVendedores")
    fields = ["nombre", "cbu"]
    
class VendedorDeleteView(LoginRequiredMixin, DeleteView):
    model = Vendedor
    template_name = "appmuebleria/vendedor_borrar.html"
    success_url = reverse_lazy("leerVendedores")

#CLIENTE

class ClienteListView (LoginRequiredMixin, ListView):
    model = Cliente
    context_object_name = "clientes"
    template_name = "appmuebleria/cliente_lista.html"
    
class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = "appmuebleria/cliente_detalle.html"
    
class ClienteCreateView (LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = "appmuebleria/cliente_crear.html"
    success_url = reverse_lazy("leerClientes")
    fields = ["nombre", "direccion", "telefono", "email"]

class ClienteUpdateView (LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = "appmuebleria/cliente_editar.html"
    success_url = reverse_lazy("leerClientes")
    fields = ["nombre", "direccion", "telefono", "email"]
    
class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = "appmuebleria/cliente_borrar.html"
    success_url = reverse_lazy("leerClientes")

#PRODUCTOS

class ProductoListView (LoginRequiredMixin, ListView):
    model = Producto
    context_object_name = "productos"
    template_name = "appmuebleria/producto_lista.html"
    
class ProductoDetailView(LoginRequiredMixin, DetailView):
    model = Producto
    template_name = "appmuebleria/producto_detalle.html"
    
class ProductoCreateView (LoginRequiredMixin, CreateView):
    model = Producto
    template_name = "appmuebleria/producto_crear.html"
    success_url = reverse_lazy("leerProductos")
    fields = ["codigo", "descripcion", "precio"]

class ProductoUpdateView (LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = "appmuebleria/producto_editar.html"
    success_url = reverse_lazy("leerProductos")
    fields = ["codigo", "descripcion", "precio"]
    
class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = "appmuebleria/producto_borrar.html"
    success_url = reverse_lazy("leerProductos")
