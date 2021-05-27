from django.contrib import admin
from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'price', 'quantity']
    ordering = ['id']
    list_display = ['id', 'name', 'price', 'quantity']
