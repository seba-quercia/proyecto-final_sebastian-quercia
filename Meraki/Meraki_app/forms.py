from django import forms
from .models import Producto, Stock, Precio

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'imagen_url']
        widgets = {
            'descripcion': forms.Textarea(attrs={
                'rows': 3,
                'style': 'resize: none;',
            })
        }
    def clean_imagen_url(self):
        url = self.cleaned_data.get('imagen_url')
        if url and not url.startswith('http'):
            raise forms.ValidationError("La URL de la imagen debe ser válida y comenzar con 'http' o 'https'.")
        return url

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