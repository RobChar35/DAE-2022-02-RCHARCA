from django.shortcuts import redirect, render, get_object_or_404

from tienda.models import Producto, Categoria

# Create your views here.
def index(request):
    lista_productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    context = {
        'productos': lista_productos,
        'categorias': categorias
    }
    return render(request, 'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categorias = Categoria.objects.all()
    context = {
        'producto': producto,
        'categorias': categorias
    }
    return render(request, 'producto.html', context)

def categoriaProducto(request, categoria_id):
    if(Categoria.objects.filter(pk=categoria_id)):
        productos = Producto.objects.filter(categoria=categoria_id)
        categorias = Categoria.objects.all()
        context = {
            'productos': productos,
            'categorias':categorias
            
        }
        return render(request, 'categoria.html', context)
    else:
        return redirect('index')
