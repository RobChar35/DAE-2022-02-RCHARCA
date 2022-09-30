from django.shortcuts import render, get_object_or_404

from tienda.models import Producto

# Create your views here.
def index(request):
    lista_productos = Producto.objects.all()
    context = {
        'productos': lista_productos
    }
    return render(request, 'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'producto.html', {'producto': producto})