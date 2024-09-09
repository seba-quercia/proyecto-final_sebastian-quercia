from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Producto, Stock, Precio
from .forms import ProductoForm, StockForm, PrecioForm


def inicio(request):
    return render(request, 'meraki_app/base.html')

class InventarioListView(ListView):
    model = Producto
    template_name = 'meraki_app/inventario.html'
    context_object_name = 'productos'

    def get_queryset(self):
        return Producto.objects.order_by('nombre')

class ProductoSearchView(ListView):
    model = Producto
    template_name = 'meraki_app/search.html'
    context_object_name = 'inventario'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Producto.objects.filter(nombre__icontains=query)
        return Producto.objects.none()

class InventarioDetailView(LoginRequiredMixin, DetailView):
    model = Producto
    template_name = 'meraki_app/producto_detalle.html'
    context_object_name = 'producto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stock'] = Stock.objects.filter(producto=self.object).first()
        context['precio'] = Precio.objects.filter(producto=self.object).first()
        context['editable'] = self.request.user.has_perm('Meraki_app.change_producto') or self.request.user.has_perm('Meraki_app.delete_producto')
        return context

class InventarioCreateView(PermissionRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'meraki_app/agregar_producto.html'
    success_url = reverse_lazy('inventario')
    permission_required = 'Meraki_app.add_producto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Producto'
        context['stock_form'] = StockForm()  
        context['precio_form'] = PrecioForm()  
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        stock_form = StockForm(self.request.POST)
        if stock_form.is_valid():
            stock = Stock(producto=self.object, cantidad=stock_form.cleaned_data['cantidad'])
            stock.save()
        
        precio_form = PrecioForm(self.request.POST)
        if precio_form.is_valid():
            precio = Precio(producto=self.object, precio=precio_form.cleaned_data['precio'])
            precio.save()
        
        return response

class InventarioUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'meraki_app/producto_detalle.html'
    success_url = reverse_lazy('inventario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Producto'
        context['stock_form'] = StockForm(instance=Stock.objects.filter(producto=self.object).first())
        context['precio_form'] = PrecioForm(instance=Precio.objects.filter(producto=self.object).first())
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        stock_form = StockForm(self.request.POST, instance=Stock.objects.filter(producto=self.object).first())
        if stock_form.is_valid():
            stock = stock_form.save(commit=False)
            stock.producto = self.object
            stock.save()
        
        precio_form = PrecioForm(self.request.POST, instance=Precio.objects.filter(producto=self.object).first())
        if precio_form.is_valid():
            precio = precio_form.save(commit=False)
            precio.producto = self.object
            precio.save()
        
        return response

    
class InventarioDeleteView(DeleteView):
    model = Producto
    template_name = 'meraki_app/confirm_delete.html'
    success_url = reverse_lazy('inventario')

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class AboutView(TemplateView):
    template_name = 'meraki_app/about.html'