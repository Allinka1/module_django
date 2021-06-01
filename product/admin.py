from django.contrib import admin
from product.models import Product

admin.site.disable_action('delete_selected')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'price', 'quantity']
    ordering = ['id']
    list_display = ['id', 'name', 'description', 'price', 'quantity']
    list_display_links = ['name']
    # list_editable = ['name', 'description', 'price', 'quantity']

    def has_delete_permission(self, request, obj=None):
        return False
