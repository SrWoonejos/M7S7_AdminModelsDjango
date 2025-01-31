from django.contrib import admin
from .models import Manufacturer, Product

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'f_vencimiento', 'manufacturer')
    list_filter = ('manufacturer', 'f_vencimiento')
    search_fields = ('name', 'description')