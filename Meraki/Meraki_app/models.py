from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    imagen_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Stock(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'{self.producto.nombre} - {self.cantidad} unidades'

class Precio(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.producto.nombre} - {self.precio} $'