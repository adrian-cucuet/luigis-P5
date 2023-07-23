from django.shortcuts import render, redirect
from .forms import ContactUsForm
from .models import ContactUs


def contact_us(request):
    """ View to render contact us page """
    
    contact_form = ContactUsForm()

    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('contact_success')
    else:
        contact_form = ContactUsForm()

    context = {
        'contact_form': contact_form
    }

    return render(request, 'contact/contact_us.html', context)


def contact_success(request):
    """ Render the Contact Success HTML page """

    return render(request, 'contact/contact_success.html')
