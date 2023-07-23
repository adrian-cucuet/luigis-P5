from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Reservation
from .forms import ReservationForm

from django.http import JsonResponse
from datetime import datetime, timedelta
from django.contrib import messages


def about(request):

    booking_form = ReservationForm()

    context = {
        'booking_form': booking_form,
    }

    return render(request, 'about/about.html', context)


def reservation_success(request):
    """ Ajax view for reservation success """
    booking_form = ReservationForm(request.POST)

    context = {
        'name': request.POST['name'],
        'phone': request.POST['phone'],
        'email': request.POST['email'],
        'no_of_guests': request.POST['no_of_guests'],
        'date': request.POST['date'],
        'time': request.POST['time'],
    }   
    if booking_form.is_valid():
        booking_form.save()

        return JsonResponse(
            {
                'bool': True,
                'context': context,
            }
        )
    else:
        # Return an error message
        messages.error(request, 'There was an error with your form. \
            Please double check your information.')
        return HttpResponse('There was an error submitting the form.')
