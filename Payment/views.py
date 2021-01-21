from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Order.models import Order
from .models import ShippingAddress
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
    return render(request, "Payment/billing_address.html", {'form': form})


def delivery_method(request):
    return HttpResponse("Delivery Method")


def payment(request):
    return HttpResponse("Payment Method")


def order_review(request):
    return HttpResponse("Order Review")