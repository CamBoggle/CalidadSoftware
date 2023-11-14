from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#CREAMOS LA CLASE DEL FORMULARIO

class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo','nombre','descripcion','precio','stock','categoria', 'imagen']
        labels = {
            'codigo': 'Codigo',
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'precio': 'Precio',
            'stock': 'Stock',
            'categoria': 'Categoria',
            'imagen': 'Imagen',
        },
        widgets = {
            'codigo' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder': 'Ingrese codigo...',
                    'id' : 'codigo',
                }
            ),
            'nombre' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder': 'Ingrese nombre...',
                    'id' : 'nombre', 
                }
            ),
            'descripcion' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder': 'Escriba descripcion...',
                    'id' : 'descripcion', 
                }
            ),
            'precio' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder': 'Ingrese precio...',
                    'id' : 'precio',
                }
            ),
            'stock' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder': 'Ingrese Stock...',
                    'id' : 'stock',
                }
            ),
            'categoria' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                    'id' : 'categoria',
                }
            ),
            'imagen': forms.FileInput( #metodo para poder modificar imagen
                attrs = {
                    'class' : 'form-control',
                    'id' : 'imagen',
                }
            )
        }