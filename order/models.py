from django.db import models
from django.urls import reverse_lazy

class Order(models.Model):

    PENDING = 1
    CONFIRMED = 2
    REJECTED = 3


    ORDER_STATUSES = [

        [PENDING, "Pending"],
        [CONFIRMED, "Confirmed"],
        [REJECTED, "Rejected"]
        
    ]


    id = models.BigAutoField(primary_key=True)
    status = models.IntegerField(choices=ORDER_STATUSES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.PositiveIntegerField()
    customer = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    product = models.ForeignKey("product.Product", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "order"
        verbose_name = "order"
        verbose_name_plural = "orders"

    def __repr__(self):
        return f"<Order ({self.id})>"

    def __str__(self):
        return f"{self.product} ({self.quantity})"

    def get_absolute_url(self):
        return reverse_lazy("order:detail", kwargs={"pk": self.pk})



