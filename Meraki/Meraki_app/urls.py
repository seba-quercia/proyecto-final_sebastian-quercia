from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # página de inicio
    path('inventario/', views.inventario, name='inventario'),  # lista de productos
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('search/', views.search, name='search'),  # detalles del producto (boton "Buscar")

]