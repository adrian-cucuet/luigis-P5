from django.shortcuts import render
from products.models import Product, Category


def index(request):
    """ A view to return the index page """
    products = Product.objects.all()
    categories = Category.objects.all()
    pizza_products = Product.objects.filter(category__id=1)

    context = {
        'products': products,
        'categories': categories,
        'pizza_products': pizza_products,
    }

    return render(request, 'home/index.html')
