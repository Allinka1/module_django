from django.db import models
from django.urls import reverse_lazy


class Refund(models.Model):

    PENDING = 1
    CONFIRMED = 2
    REJECTED = 3


    REFUND_STATUSES = [

        [PENDING, "Pending"],
        [CONFIRMED, "Confirmed"],
        [REJECTED, "Rejected"]
        
    ]

    id = models.AutoField(primary_key=True)
    status = models.IntegerField(choices=REFUND_STATUSES, default=1)
    order = models.OneToOneField("order.Order", on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.order}'

    def __repr__(self):
        return f'<Refund ("{self.id}")>'

    def get_absolute_url(self):
        return reverse_lazy("order:list")
