import datetime
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model): 
    idCategoria = models.IntegerField(primary_key = True, verbose_name="Id de Categoria")
    nombreCategoria = models.CharField(max_length = 50, blank = True, verbose_name = "Nombre de Categoria")

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    codigo = models.CharField(primary_key = True, max_length = 8, verbose_name = "Codigo")
    nombre = models.CharField(max_length = 50, blank = True, verbose_name = "Nombre")
    descripcion = models.CharField(max_length = 250, blank = True, verbose_name = "Descripcion")
    precio = models.DecimalField(max_digits = 10, decimal_places= 0, verbose_name = "Precio")
    stock = models.DecimalField(max_digits = 10, decimal_places= 0, verbose_name = "stock")
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE, verbose_name = "Categoria")

    def __str__(self):
        return self.nombre
    

#Creamos modelo de boleta
class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)
    
    def __str__(self):
        return str(self.id_boleta)

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)