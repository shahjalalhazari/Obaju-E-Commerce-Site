from django.db import models
from django.conf import settings
from Store.models import Product


# CART MODEL
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} X {self.product}'

    # FOR GET TOTAL ANY PRODUCT
    def get_total(self):
        total = self.product.price * self.quantity
        float_total = format(total, '0.2f')
        return float_total


# ORDER MODEL
class Order(models.Model):
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    paymentId = models.CharField(max_length=300, blank=True, null=True)
    orderId = models.CharField(max_length=300, blank=True, null=True)

    # FOR GET TOTAL OF WHOLE CART
    def get_total_amout(self):
        total = 0
        for item in self.orderitems.all():
            total += float(item.get_total())
        return total
