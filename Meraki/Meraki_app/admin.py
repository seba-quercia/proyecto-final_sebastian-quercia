from django.contrib import admin
from Meraki_app.models import Producto, Stock, Precio


# Register your models here.
admin.site.register(Producto)
admin.site.register(Stock)
admin.site.register(Precio)
