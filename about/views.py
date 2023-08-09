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
    }

    return render(request, 'about/about.html', context)


def reservation_success(request):
    """ Render the Contact Success HTML page """

    return render(request, 'about/reservation_success.html')


def bookings(request):
    """ Display the user's profile. """
    today = datetime.today()

    # Get all bookings scheduled for today or later
    bookings = Reservation.objects.filter(date__gte=today)

    # Order the bookings by date
    bookings = bookings.order_by('date')

    context = {
        'bookings': bookings,
    }

    return render(request, 'bookings/bookings.html', context)