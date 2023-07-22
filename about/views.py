from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Reservation
from .forms import ReservationForm
from datetime import datetime, timedelta
from django.contrib import messages


def about(request):

    booking_form = ReservationForm()

    context = {
        'booking_form': booking_form,
    }

    return render(request, 'about/about.html', context)


def reservation_success(request):
    if request.method == 'POST':
        form_data = {
            'name': request.POST['name'],
            'phone': request.POST['phone'],
            'email': request.POST['email'],
            'no_of_guests': request.POST['no_of_guests'],
            'date': request.POST['date'],
            'time': request.POST['time'],
        }
        booking_form = ReservationForm(form_data)
        if booking_form.is_valid():
            reservation = booking_form.save(commit=False)
            reservation.save()

            messages.success(request, 'Reservation created successfully! \
                An email with the detail will be sent soon.')

            context = {
                        'reservation': reservation,
                    }

            return render(request, 'about/reservation_success.html', context)
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        booking_form = ReservationForm()

    context = {
                'reservation': reservation,
            }

    return render(request, 'about/reservation_success.html', context)
