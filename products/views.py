from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages
from django.db.models import Q


from .models import Product
from .forms import ProductForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Oops, you must include a cool pizza name!")
                return redirect(reverse('menu'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/menu.html', context)


def menu_item(request, product_id):
    """ A view to show an individual item """

    product = get_object_or_404(Product, pk=product_id)
    similar_products = Product.objects.filter(category=product.category).exclude(pk=product_id)[:5]

    context = {
        'product': product,
        'similar_products': similar_products,
    }

    return render(request, 'products/menu_item.html', context)


def add_product(request):
    """ Add a product to the store """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
