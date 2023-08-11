from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.db.models import Avg

from .models import Product, ProductReview, Category
from .forms import ProductForm, ProductReviewForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    categories = Category.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Oops, you must \
                     include a cool pizza name!")
                return redirect(reverse('menu'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'categories': categories,
    }

    return render(request, 'products/menu.html', context)


def menu_item(request, product_id):
    """ A view to show an individual item """

    product = get_object_or_404(Product, pk=product_id)
    # Getting similar products from the same category
    similar_products = Product.objects.filter(
        category=product.category).exclude(pk=product_id)[:5]
    # Getting all reviews related to a products
    reviews = ProductReview.objects.filter(product=product).order_by("-date")
    # Getting average reviews
    average_rating = ProductReview.objects.filter(
        product=product).aggregate(rating=Avg('rating'))
    # Product review form
    review_form = ProductReviewForm()

    make_review = True
    if request.user.is_authenticated:
        user_review_count = ProductReview.objects.filter(
            user=request.user.id, product=product).count()
        if user_review_count > 0:
            make_review = False

    context = {
        'product': product,
        'make_review': make_review,
        'review_form': review_form,
        'average_rating': average_rating,
        'reviews': reviews,
        'similar_products': similar_products,
    }

    return render(request, 'products/menu_item.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('menu_item', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
                 Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('menu_item', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                 Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('menu'))


def ajax_add_review(request, product_id):
    """ Add a review and rating to individual product """
    product = Product.objects.get(pk=product_id)
    user = request.user

    review = ProductReview.objects.create(
        user=user,
        product=product,
        review=request.POST['review'],
        rating=request.POST['rating'],
    )

    context = {
        'user': user.username,
        'review': request.POST['review'],
        'rating': request.POST['rating'],
    }

    average_reviews = ProductReview.objects.filter(
        product=product).aggregate(rating=Avg('rating'))

    return JsonResponse(
        {
            'bool': True,
            'context': context,
            'average_reviews': average_reviews,
        }
    )
