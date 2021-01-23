from django.contrib import admin
from .models import Cart, Order, DeliveryMethod


admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(DeliveryMethod)