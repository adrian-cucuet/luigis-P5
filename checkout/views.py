from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Looks like your cart is empty")
        return redirect(reverse('menu'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form
    }

    return render(request, template, context)
