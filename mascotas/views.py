from django.shortcuts import render, redirect
from .models import Producto, Categoria, Boleta, detalle_boleta
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required #para restringir el uso de metodos
from .forms import ProductoForm, RegistroUserForm
from django.contrib.auth import authenticate,login
from mascotas.compra import Carrito
# Create your views here.
def inicio(request):
    return render(request,'Inicio.html')

def perros(request):
    return render(request, 'Perros.html')

def quienes(request):
    return render(request, 'QuienesSomos.html')

def donaciones(request):
    return render(request, 'Donaciones.html')

def gatos(request):
    productos = Producto.objects.all() #Trae TODOS los datos del objeto como una consulta SELECT
    datos = {'productos' : productos}
    return render(request, 'Gatos.html', datos)

#CRUD
def crear(request):
    if request.method=="POST":
        productoform = ProductoForm(request.POST, request.FILES)
        if productoform.is_valid():
            productoform.save()     #similar al insert
            return redirect('gatos')
    else:
        productoform=ProductoForm()
    return render(request, 'Crear.html', {'productoform':productoform})

@login_required #restringimos el uso de esa opcion SOLO cuando esta logeado
def eliminar(request, id):
    productoEliminado = Producto.objects.get(codigo=id) #Obtenemos un objeto por su ID
    productoEliminado.delete()
    return redirect('gatos')

@login_required
def modificar(request, id):
    producto = Producto.objects.get(codigo=id)
    datos = { #CREAMOS DICCIONARIO
        'form': ProductoForm(instance = producto) #Devuelve el objeto instanciado deacuerdo a la patente
    }
    if(request.method == "POST"):
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if(formulario.is_valid()):
            formulario.save()
            return redirect('gatos')
    return render(request, 'Modificar.html', datos)

def registrar(request):
    data={                          #parámetro que llega al template
        'form': RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()       #crear un objeto en el backend
            user = authenticate(username=formulario.cleaned_data["username"], 
                    password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect('inicio') 
        data["form"]=formulario           
    return render(request, 'registration/registrar.html',data)



def tienda(request):
    productos = Producto.objects.all() #Trae TODOS los datos del objeto como una consulta SELECT
    datos = {'productos' : productos}
    return render(request, 'Tienda.html', datos)

#CARRITO
def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(codigo=id)
    carrito_compra.agregar(producto=producto)
    return redirect('tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(codigo=id)
    carrito_compra.eliminar(producto=producto)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(codigo=id)
    carrito_compra.restar(producto=producto)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')    


def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Producto.objects.get(codigo = value['producto_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html',datos)
