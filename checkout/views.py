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
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51N9XkEH0nZPjsVFWudaO0OYlY6o7c0gsslK1x65ZKh70kyyyvT9SzjvkSr9T3Wr73cHKQLRHs9Croxe52IOMKDa900rkirCMyV',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
