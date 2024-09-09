from django.urls import path
from django.contrib.auth.views import LogoutView
from user.views import *

urlpatterns = [
    
    path("login/", login_request, name="login"),
    path("register/", register, name="register"),
    path("logout/", LogoutView.as_view(template_name = "user/logout.html"), name="logout"),
    path("edit_user/", editar_perfil, name="edit_user"),
    path("edit_pass/", CambiarPass.as_view(), name="edit_pass")
    
]