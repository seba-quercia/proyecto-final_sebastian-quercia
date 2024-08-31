from django import forms
from .models import Producto, Stock, Precio

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={
                'rows': 3,
                'style': 'resize: none;',
            })
        }

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['cantidad']
        widgets = {
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la cantidad',
            })
        }

class PrecioForm(forms.ModelForm):
    class Meta:
        model = Precio
        fields = ['precio']
        widgets = {
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el precio',
            })
        }