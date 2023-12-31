from django.shortcuts import render, redirect
from .forms import ContactUsForm
from django.contrib import messages


def contact_us(request):
    """ View to render contact us page """

    contact_form = ContactUsForm()

    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Message sent successfully.')
            return redirect('contact_success')
        else:
            messages.error(request, 'Please ensure the form is completed')

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact/contact_us.html', context)


def contact_success(request):
    """ Render the Contact Success HTML page """

    return render(request, 'contact/contact_success.html', {
        'on_contact_page': True})
