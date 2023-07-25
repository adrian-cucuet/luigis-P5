from django.shortcuts import render, redirect, reverse
from .models import Reservation
from .forms import ReservationForm
from django.contrib import messages


def about(request):
    """ View to render contact us page """
    booking_form = ReservationForm()

    if request.method == 'POST':
        booking_form = ReservationForm(request.POST)
        if booking_form.is_valid():
            booking_form.save()
            messages.success(request, f'Reservation successfully created!')
            return redirect('reservation_success')

    else:
        booking_form = ReservationForm()

    context = {
        'booking_form': booking_form,
    }

    return render(request, 'about/about.html', context)


def reservation_success(request):
    """ Render the Contact Success HTML page """

    return render(request, 'about/reservation_success.html')
