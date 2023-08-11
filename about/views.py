from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.contrib import messages


def about(request):
    """ View to render contact us page """
    booking_form = ReservationForm()

    if request.method == 'POST':
        booking_form = ReservationForm(request.POST)
        if booking_form.is_valid():
            booking_form.save()
            messages.success(request, 'Reservation successfully created!')
            return redirect('reservation_success')

        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        booking_form = ReservationForm()

    context = {
        'booking_form': booking_form,
        'on_booking_page': True,
    }

    return render(request, 'about/about.html', context)


def reservation_success(request):
    """ Render the Contact Success HTML page """

    return render(request, 'about/reservation_success.html')
