from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # página de inicio
    path('productos/', views.productos, name='productos'),  # lista de productos
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('search/', views.search, name='search'),  # detalles del producto (boton "Buscar")
    path('stock/', views.stock, name='stock'),  # manejo de stock
    path('precios/', views.precios, name='precios'),  # manejo de precios
]