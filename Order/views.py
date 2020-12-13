from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, Order
from Store.models import Product


# ADD PRODUCT TO CART VIEW
@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_item = Cart.objects.get_or_create(product=product, user=request.user, purchased=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(product=product).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request, "This item quantity was updated!")
            return HttpResponseRedirect(reverse('store:product_detail', kwargs={'pk': product.pk}))
        else:
            order.orderitems.add(order_item[0])
            messages.success(request, "This product has been added to your cart!")
            HttpResponseRedirect(reverse('store:product_detail', kwargs={'pk': product.pk}))
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        messages.success(request, "This product has been added to your cart!")
        HttpResponseRedirect(reverse('store:product_detail', kwargs={'pk': product.pk}))


# CART VIEW
@login_required
def cart_view(request):
    carts = Cart.objects.filter(user=request.user, purchased=False)
    orders = Order.objects.filter(user=request.user, ordered=False)
    if carts.exists() and orders.exists():
        order = orders[0]
        return render(request, 'Order/cart.html', {'carts': carts, 'order': order})
    else:
        messages.warning(request, "You don't have any item in your cart.")
        return redirect("store:home")