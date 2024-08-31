from django import forms
from .models import Producto, Stock, Precio

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion']

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['producto', 'cantidad']

class PrecioForm(forms.ModelForm):
    class Meta:
        model = Precio
        fields = ['producto', 'precio']