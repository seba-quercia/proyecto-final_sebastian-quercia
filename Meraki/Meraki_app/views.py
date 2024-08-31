from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Stock, Precio
from .forms import ProductoForm, StockForm, PrecioForm

def inicio(request):
    return render(request, 'meraki_app/base.html')

def inventario(request):
    if request.method == 'POST':
        if 'modificar_producto' in request.POST:
            # Modificar un producto existente
            producto_id = request.POST.get('producto_id')
            producto = get_object_or_404(Producto, id=producto_id)
            form = ProductoForm(request.POST, instance=producto)
            stock_form = StockForm(request.POST, instance=Stock.objects.filter(producto=producto).first())
            precio_form = PrecioForm(request.POST, instance=Precio.objects.filter(producto=producto).first())
            
            if form.is_valid() and stock_form.is_valid() and precio_form.is_valid():
                form.save()

                # Guardar o actualizar stock
                stock_instance = Stock.objects.filter(producto=producto).first()
                if stock_instance:
                    stock_instance.cantidad = stock_form.cleaned_data['cantidad']
                    stock_instance.save()
                else:
                    Stock.objects.create(producto=producto, cantidad=stock_form.cleaned_data['cantidad'])

                # Guardar o actualizar precio
                precio_instance = Precio.objects.filter(producto=producto).first()
                if precio_instance:
                    precio_instance.precio = precio_form.cleaned_data['precio']
                    precio_instance.save()
                else:
                    Precio.objects.create(producto=producto, precio=precio_form.cleaned_data['precio'])

                return redirect('inventario')

        elif 'agregar_producto' in request.POST:
            # Agregar un nuevo producto
            form = ProductoForm(request.POST)
            stock_form = StockForm(request.POST)
            precio_form = PrecioForm(request.POST)
            
            if form.is_valid() and stock_form.is_valid() and precio_form.is_valid():
                producto = form.save()
                
                # Crear y guardar stock
                Stock.objects.create(producto=producto, cantidad=stock_form.cleaned_data['cantidad'])
                
                # Crear y guardar precio
                Precio.objects.create(producto=producto, precio=precio_form.cleaned_data['precio'])
                
                return redirect('inventario')
    elif 'edit' in request.GET:
        # Editar un producto existente
        producto_id = request.GET.get('edit')
        producto = get_object_or_404(Producto, id=producto_id)
        form = ProductoForm(instance=producto)
        stock_instance = Stock.objects.filter(producto=producto).first()
        precio_instance = Precio.objects.filter(producto=producto).first()
        stock_form = StockForm(instance=stock_instance) if stock_instance else StockForm()
        precio_form = PrecioForm(instance=precio_instance) if precio_instance else PrecioForm()
    else:
        form = ProductoForm()
        stock_form = StockForm()
        precio_form = PrecioForm()

    productos = Producto.objects.all()
    stock_list = Stock.objects.all()
    precio_list = Precio.objects.all()

    return render(request, 'meraki_app/inventario.html', {
        'productos': productos,
        'form': form,
        'stock_form': stock_form,
        'precio_form': precio_form,
        'stock_list': stock_list,
        'precio_list': precio_list,
    })

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('inventario')

def search(request):
    query = request.GET.get('q', '')
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = Producto.objects.none()

    return render(request, 'meraki_app/search.html', {
        'inventario': productos,
    })
