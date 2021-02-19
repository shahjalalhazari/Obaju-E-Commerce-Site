from django.conf import settings
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Order.models import Order, Cart
from .models import ShippingAddress, DeliveryMethod, PaymentMethod
from .forms import ShippingAddressForm


# BIILLING ADDRESS VIEW
@login_required
def shipping_address(request):
    saved_address = ShippingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    form = ShippingAddressForm(instance=saved_address)
    if request.method == "POST":
        form = ShippingAddressForm(request.POST, instance=saved_address)
        if form.is_valid():
            form.save()
            messages.success(request, "Address saved!")
            return HttpResponseRedirect(reverse("payment:delivery_method"))
    context = {
        'form': form
    }
    return render(request, "Payment/shipping_address.html", context)


# DELIVERY METHOD VIEW
@login_required
def delivery_method(request):
    delivery_methods = DeliveryMethod.objects.all()
    if request.method == "POST":
        selected_option = request.POST.get('selected_option') # get selected delivery method from user
        delivery_method = DeliveryMethod.objects.get(pk=selected_option) # find the selected option
        order_qs = Order.objects.get(user=request.user, ordered=False) # get current order of this user
        order_qs.delivery_method = delivery_method # add selected payment method to current order's payment method
        order_qs.save()
        messages.success(request, "Delivery method selected!")
        return HttpResponseRedirect(reverse("payment:payment"))
    context = {
        'delivery_methods': delivery_methods
    }
    return render(request, "Payment/delivery_method.html", context)


# PAYMENT METHOD VIEW
@login_required
def payment(request):
    payment_methods = PaymentMethod.objects.all()
    if request.method == "POST":
        selected_option = request.POST.get('selected_option') # get selected payment method from user
        payment_method = PaymentMethod.objects.get(slug=selected_option) # find the selected option
        order_qs = Order.objects.get(user=request.user, ordered=False) # get current order of this user
        order_qs.payment_method = payment_method # add selected delivery method to current order's delivery method
        order_qs.save()
        messages.success(request, "Payment method selected!")
        return HttpResponseRedirect(reverse("payment:order_review"))
    context = {
        'payment_methods': payment_methods
    }
    return render(request, "Payment/payment.html", context)


# ORDER REVIEW VIEW
@login_required
def order_review(request):
    carts = Cart.objects.filter(user=request.user, purchased=False)
    order = Order.objects.filter(user=request.user, ordered=False)[0]
    payment_method = order.payment_method
    delivery_method = order.delivery_method
    checkout = True
    if payment_method.slug == "cod":
        checkout = False
    context = {
        'carts': carts,
        'order': order,
        'checkout': checkout,
        'delivery_method': delivery_method,
    }
    return render(request, "Payment/order_review.html", context)