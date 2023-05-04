from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Producto, Categoria
# Create your views here.
def index(request):
    lista_productos = Producto.objects.order_by('nombre')[:6]
    lista_categorias = Categoria.objects.all()
    context = {
        'productos':lista_productos,
        'categorias':lista_categorias
        }
    return render(request,'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request,'producto.html',{'producto': producto})

def categoria(request,categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    lista_productos = categoria.producto_set.all()
    lista_categorias = Categoria.objects.all()
    
    context = {
        'productos':lista_productos,
        'categorias':lista_categorias,
        'categoria':categoria
    }
    
    return render(request,'index.html',context)
