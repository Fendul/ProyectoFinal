from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from user.forms import *
from user.models import *

# Create your views here.

def login_request(request):
    
    mensaje = ""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get ("username")
            clave = form.cleaned_data.get ("password")

            user = authenticate(username=usuario, password=clave)

            if usuario is not None:
                login(request, user)
                return render (request, "appmuebleria/inicio.html")
            
        mensaje = "Usuario o contraseña incorrectos"
        
    form = AuthenticationForm()
    return render (request, "user/login.html", {"form" : form, "mensaje" : mensaje})

def register (request):
    
    mensaje =""
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            return render (request, "appmuebleria/inicio.html")
        
        else:
            mensaje ="Error en los datos"
            mensaje += f" | {form.errors}"

    form = UserRegisterForm()    
    return render (request, "user/register.html" , {"form" : form , "mensaje" : mensaje})

@login_required
def editar_perfil(request):
    
    usuario = request.user
    
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)
        if miFormulario.is_valid():
            
            if miFormulario.cleaned_data.get("Avatar"):
                
                if Avatar.objects.filter(user=usuario).exists():
                    
                    usuario.imagen.imagen = miFormulario.cleaned_data.get('Avatar')
                    usuario.imagen.save()
                    
                else:
                    
                    avatar = Avatar(user=usuario, imagen=miFormulario.cleaned_data.get('Avatar'))
                    avatar.save()
                    
            miFormulario.save()

            return render(request, "appmuebleria/inicio.html")

    else:
        miFormulario = UserEditForm(instance=usuario)

    return render(request, "user/edit_user.html", {"mi_form": miFormulario, "usuario": usuario})

class CambiarPass(LoginRequiredMixin, PasswordChangeView):
    template_name = "user/edit_pass.html"
    success_url = reverse_lazy("edit_user")