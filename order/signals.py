from django.dispatch import receiver
from django.db.models.signals import pre_save
from order.models import Order
from product.models import Product
from user.models import UserProfile
import pdb

@receiver(pre_save, sender=Order)
def pre_order(sender, instance, *args, **kwargs):
    total_price = instance.product.price * instance.quantity
    user_wallet = instance.customer.userprofile.wallet
    UserProfile.objects.filter(id=instance.customer.userprofile.id).update(wallet=user_wallet - total_price)
    Product.objects.filter(id=instance.product.id).update(quantity=instance.product.quantity - instance.quantity)

