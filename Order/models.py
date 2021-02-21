import uuid
from django.db import models
from django.conf import settings
from Store.models import Product
from Payment.models import DeliveryMethod, PaymentMethod


# CART MODEL
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} X {self.product}'

    # GET TOTAL FOR EACH PRODUCT
    def get_cart_total(self):
        total = self.product.price * self.quantity
        float_cart_total = format(total, '0.2f')
        return float_cart_total


# ORDER MODEL
class Order(models.Model):
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='order_user')
    ordered = models.BooleanField(default=False)
    paymentId = models.UUIDField(primary_key=False, default=uuid.uuid1, editable=False)
    validId = models.UUIDField(primary_key=False, default=uuid.uuid1, editable=False)
    orderId = models.UUIDField(primary_key=False, default=uuid.uuid1, editable=False)
    delivery_method = models.ForeignKey(DeliveryMethod, on_delete=models.SET_NULL, null=True, blank=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # GET SUB TOTAL OF A ORDER
    def get_order_sub_total(self):
        total = 0
        for item in self.orderitems.all():
            total += float(item.get_cart_total())
            float_total_amount = format(total, '0.2f')
        return float_total_amount
    
    # GET TOTAL AMOUNT OF A ORDER WITH DELIVERY COST
    def get_total_amount(self):
        order_sub_total = self.get_order_sub_total()
        delivery_cost = self.delivery_method.cost
        total = format(float(order_sub_total) + float(delivery_cost), '0.2f')
        return total

    def __str__(self):
        return f"{self.user}'s order"