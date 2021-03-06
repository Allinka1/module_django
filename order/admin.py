from django.contrib import admin

from order.models import Order


def get_product_quantity(order):
    return order.product.quantity


def get_product_name(order):
    return str(order.product)


def get_prepare_order(order):
    return order.quantity < order.product.quantity


def get_order_identifier(order):
    return f"{order.customer.username}-{order.id}"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    fields = ["status"]

    list_display = [
        get_order_identifier,
        "created_at",
        "updated_at",
        get_product_name,
        get_product_quantity,
        "quantity",
        get_prepare_order,
        "status",
    ]
    list_editable = ["quantity", "status"]
    ordering = ["created_at", "updated_at"]
