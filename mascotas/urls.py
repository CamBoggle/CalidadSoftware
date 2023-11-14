from django.urls import path
from .views import inicio, perros, quienes, donaciones, gatos, crear, eliminar, modificar, registrar, tienda, agregar_producto,eliminar_producto,restar_producto,limpiar_carrito,generarBoleta

urlpatterns=[
    path('', inicio, name="inicio"),
    path('perros/', perros, name="perros"),
    path('quienes/', quienes, name="quienes"),
    path('donaciones/', donaciones, name="donaciones"),
    path('gatos/', gatos, name="gatos"),
    path('crear/', crear, name="crear"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>',modificar, name="modificar"),
    path('registrar/', registrar, name="registrar"),

    path('tienda/', tienda, name="tienda"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
    path('generarBoleta/', generarBoleta,name="generarBoleta"),


]
