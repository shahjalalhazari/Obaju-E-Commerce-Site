from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Order.models import Order
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
    return render(request, "Payment/shipping_address.html", {'form': form})


# DELIVERY METHOD VIEW
@login_required
def delivery_method(request):
    delivery_methods = DeliveryMethod.objects.all()
    if request.method == "POST":
        selected_option = request.POST.get('selected_option') # get selected delivery method from user
        delivery_method = DeliveryMethod.objects.get(pk=selected_option) # find the selected option
        order_qs = Order.objects.get(user=request.user, ordered=False) # get current order of this user
        order_qs.delivery_method = delivery_method # add selected delivery method to current order's delivery method
        order_qs.save()
        messages.success(request, "Delivery method selected!")
        return HttpResponseRedirect(reverse("payment:payment"))
    return render(request, "Payment/delivery_method.html", {'delivery_methods': delivery_methods})


def payment(request):
    payment_methods = PaymentMethod.objects.all()
    if request.method == "POST":
        selected_option = request.POST.get('selected_option') # get selected payment method from user
        payment_method = PaymentMethod.objects.get(slug=selected_option) # find the selected option
        #order_qs = Order.objects.get(user=request.user, ordered=False) # get current order of this user
        #order_qs.delivery_method = delivery_method # add selected delivery method to current order's delivery method
        #order_qs.save()
    context = {
        'payment_methods': payment_methods
    }
    return render(request, "Payment/payment.html", context)


def order_review(request):
    return HttpResponse("Order Review")