from django.contrib import admin

from refund.models import Refund


# @admin.action(description='Aproove')
# def aproove(modeladmin, request, queryset):
#     queryset.update(status=2)

# @admin.action(description='Reject')
# def reject(modeladmin, request, queryset):
#     queryset.update(status=3)


def get_order_identifier(refund):
    return f"{refund.order.customer.username}-{refund.order.id}"


@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):

    fields = ["status"]
    # actions = [aproove, reject]

    list_display = [
        get_order_identifier,
        "created_at",
        "status"
    ]

    list_editable = ["status"]
    ordering = ["created_at"]