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
            messages.info(request, "This item quantity has been updated!")
            return HttpResponseRedirect(reverse('store:product_detail', kwargs={'pk': pk}))
        else:
            order.orderitems.add(order_item[0])
            messages.success(request, 'This item has been added to your cart!')
            return HttpResponseRedirect(reverse('store:product_detail', kwargs={'pk': pk}))
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        messages.success(request, 'This item has been added to your cart!')
        return HttpResponseRedirect(reverse('store:product_detail', kwargs={'pk': pk}))


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
        return redirect("home:home")


# REMOVE FORM CART VIEW
@login_required
def remove_from_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(product=product).exists():
            order_item = Cart.objects.filter(product=product, user=request.user, purchased=False)[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            messages.warning(request, "This item has been removed from your cart!")
            return redirect('order:cart')
        else:
            messages.info(request, 'This item was not in your cart!')
            return redirect('home:home')
    else:
        messages.warning(request, "You don't have an active order.")
        return redirect('home:home')


# INCREASE ITEM QUANTITY VIEW
@login_required
def inc_qty(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(product=product).exists():
            order_item = Cart.objects.filter(product=product, user=request.user, purchased=False)[0]
            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                messages.info(request, f"{product.title} quantity has been updated!")
                return redirect('order:cart')
        else:
            messages.info(request, f"{product.title} is not in your cart.")
            return redirect('order:cart')
    else:
        messages.warning(request, "You don't have an active order.")
        return redirect('home:home')


# DECREASE ITEM QUANTITY VIEW
@login_required
def dec_qty(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(product=product).exists():
            order_item = Cart.objects.filter(product=product, user=request.user, purchased=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, f"{product.title} quantity has been updated!")
                return redirect('order:cart')
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                messages.warning(request, f"{product.title} item has been removed form your cart")
                return redirect('order:cart')
        else:
            messages.info(request, f"{product.title} is not in your cart.")
            return redirect('order:cart')
    else:
        messages.warning(request, "You don't have an active order.")
        return redirect('home:home')