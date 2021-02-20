from django.contrib import admin
from .models import ShippingAddress, DeliveryMethod, PaymentMethod

admin.site.register(ShippingAddress)
admin.site.register(DeliveryMethod)
admin.site.register(PaymentMethod)