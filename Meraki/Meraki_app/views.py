from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Stock, Precio
from .forms import ProductoForm, StockForm, PrecioForm

def inicio(request):
    return render(request, 'meraki_app/base.html')

def productos(request):
    if request.method == 'POST':
        if 'modificar_producto' in request.POST:
            # Modificar un producto existente
            producto_id = request.POST.get('producto_id')
            producto = get_object_or_404(Producto, id=producto_id)
            form = ProductoForm(request.POST, instance=producto)
            if form.is_valid():
                form.save()
                return redirect('productos')
        elif 'agregar_producto' in request.POST:
            # Agregar un nuevo producto
            form = ProductoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('productos')
    elif 'edit' in request.GET:
        # Editar un producto existente
        producto_id = request.GET.get('edit')
        producto = get_object_or_404(Producto, id=producto_id)
        form = ProductoForm(instance=producto)
    else:
        form = ProductoForm()

    # Listar todos los productos
    productos = Producto.objects.all()
    return render(request, 'meraki_app/productos.html', {
        'productos': productos,
        'form': form
    })

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')

def stock(request):
    if request.method == 'POST':
        if 'ver_stock' in request.POST:
            # Ver stock
            stocks = Stock.objects.all()
            return render(request, 'meraki_app/stock.html', {'stocks': stocks, 'ver': True})

        elif 'modificar_stock' in request.POST:
            form = StockForm(request.POST)
            if form.is_valid():
                producto = form.cleaned_data['producto']
                nuevo_stock = form.cleaned_data['cantidad']
                stock_actual = Stock.objects.filter(producto=producto).first()
                if stock_actual:
                    stock_actual.cantidad = nuevo_stock
                    stock_actual.save()
                else:
                    Stock.objects.create(producto=producto, cantidad=nuevo_stock)
                
                return redirect('stock')
    else:
        form = StockForm()

    # Renderizar vista por defecto (ver stock)
    stocks = Stock.objects.all()
    return render(request, 'meraki_app/stock.html', {
        'form': form,
        'stocks': stocks,
        'ver': True
    })

def precios(request):
    if request.method == 'POST':
        if 'ver_precios' in request.POST:
            precios = Precio.objects.all()
            return render(request, 'meraki_app/precios.html', {'precios': precios, 'ver': True})

        elif 'modificar_precios' in request.POST:
            form = PrecioForm(request.POST)
            if form.is_valid():
                producto = form.cleaned_data['producto']
                nuevo_precio = form.cleaned_data['precio']
                precio_actual = Precio.objects.filter(producto=producto).first()
                if precio_actual:
                    precio_actual.precio = nuevo_precio
                    precio_actual.save()
                else:
                    Precio.objects.create(producto=producto, precio=nuevo_precio)
                
                return redirect('precios')
    else:
        form = PrecioForm()

    # Renderizar vista por defecto (ver precios)
    precios = Precio.objects.all()
    return render(request, 'meraki_app/precios.html', {
        'form': form,
        'precios': precios,
        'ver': True
    })

def search(request):
    query = request.GET.get('q', '')
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = Producto.objects.none()

    return render(request, 'meraki_app/search.html', {
        'productos': productos,
    })
    