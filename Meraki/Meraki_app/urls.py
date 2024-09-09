from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inventario/', views.InventarioListView.as_view(), name='inventario'),
    path('producto/<int:pk>/', views.InventarioDetailView.as_view(), name='producto_detalle'),
    path('producto/nuevo/', views.InventarioCreateView.as_view(), name='agregar_producto'),
    path('producto/<int:pk>/editar/', views.InventarioUpdateView.as_view(), name='producto_editar'),
    path('producto/<int:pk>/delete/', views.InventarioDeleteView.as_view(), name='eliminar_producto'),
    path('search/', views.ProductoSearchView.as_view(), name='search'),
    path('about/', views.AboutView.as_view(), name='about'),
]
