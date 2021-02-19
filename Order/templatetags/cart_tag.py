from django import template
from Order.models import Order

register = template.Library()

@register.filter
def item_total(user):
    order = Order.objects.filter(user=user, ordered=False)
    if order.exists():
        return order[0].orderitems.count()
    else:
        return 0
    
    
@register.filter
def total_amount(user):
    order = Order.objects.filter(user=user, ordered=False)[0]
    sub_total = order.get_total_amount()
    delivery_cost = order.delivery_method.cost
    total_amount = float(sub_total) + float(delivery_cost)
    return total_amount