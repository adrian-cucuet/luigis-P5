from django.shortcuts import render, HttpResponse
from products.models import Product, Category
from django.http import JsonResponse

from .forms import NewsletterForm
from .models import Newsletter


def index(request):
    """ A view to return the index page """
    categories = Category.objects.all()
    products = Product.objects.all()
    pizza_products = Product.objects.filter(category__name='pizza')
    subscribe_form = NewsletterForm()

    context = {
        'categories': categories,
        'products': products,
        'pizza_products': pizza_products,
        'subscribe_form': subscribe_form,
    }

    return render(request, 'home/index.html', context)


def sign_up_newsletter(request):
    subscribe_form = NewsletterForm(request.POST)

    context = {
        'full_name': request.POST['full_name'],
        'email_address': request.POST['email_address'],
    }

    if subscribe_form.is_valid():
        # Save the form data
        subscribe_form.save()

        return JsonResponse(
            {
                'bool': True,
                'context': context,
            }
        )

    else:
        # Return an error message
        messages.alert(request, 'Please complete the form')
        return HttpResponse('There was an error submitting your subscription.')
