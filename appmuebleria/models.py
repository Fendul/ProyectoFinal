from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=40)
    telefono=models.IntegerField()
    email=models.EmailField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Direccion: {self.direccion} - Telefono: {self.telefono} - Email: {self.email}"
 
class Producto(models.Model):
    codigo=models.IntegerField()
    descripcion=models.CharField(max_length=50)
    precio=models.DecimalField(decimal_places=2, max_digits=9)
    
    
    def __str__(self):
        return f"Codigo: {self.codigo} - Descripcion: {self.descripcion} - Precio: {self.precio}"
    
class Vendedor(models.Model):
    nombre=models.CharField(max_length=30)
    cbu=models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - CBU: {self.cbu}"
    
    
    

       