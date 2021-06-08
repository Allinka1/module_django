from django.dispatch import receiver
from django.db.models.signals import post_save
from refund.models import Refund
from product.models import Product
from user.models import UserProfile



@receiver(post_save, sender=Refund)
def post_aproove(sender, instance, *args, **kwargs):
    if instance.status == 2:
        quantity_of_product = instance.order.quantity
        quantity_of_store = instance.order.product.quantity
        user_wallet = instance.order.customer.userprofile.wallet
        total_price = instance.order.product.price * instance.order.quantity
        UserProfile.objects.filter(id=instance.order.customer.userprofile.id).update(wallet=user_wallet + total_price)
        Product.objects.filter(id=instance.order.product.id).update(quantity=quantity_of_store + quantity_of_product)
        instance.order.delete()


@receiver(post_save, sender=Refund)
def post_reject(sender, instance, *args, **kwargs):
    if instance.status == 3:
        instance.delete()
