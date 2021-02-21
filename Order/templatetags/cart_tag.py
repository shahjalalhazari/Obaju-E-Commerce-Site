from django import template
from Order.models import Order

register = template.Library()


# ITEM(S) HAS IN USER CART
@register.filter
def item_total(user):
    order = Order.objects.filter(user=user, ordered=False)
    if order.exists():
        return order[0].orderitems.count()
    else:
        return 0
    
    
# FIRST 18 DIGITS OF ORDER ID
@register.filter
def orderId_filter(value):
    orderId = str(value)
    return orderId[:18]+"..."